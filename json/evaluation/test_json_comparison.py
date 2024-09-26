import os
import json
import csv

def is_valid_json(filepath):
    """Check if a file contains valid JSON."""
    try:
        with open(filepath, 'r') as file:
            json.load(file)
        return True
    except json.JSONDecodeError:
        return False

def load_json(filepath):
    """Load JSON data from a file."""
    with open(filepath, 'r') as file:
        return json.load(file)

def normalize_json(data):
    """Normalize JSON data by sorting lists and converting dictionaries."""
    if isinstance(data, dict):
        # Recursively normalize each dictionary key's value
        return {key: normalize_json(value) for key, value in sorted(data.items())}
    elif isinstance(data, list):
        # Sort lists after normalizing each element. Convert dictionaries in the list to sorted tuples for sorting purposes.
        return sorted([normalize_json(item) for item in data], key=lambda x: str(x))
    return data  # Return primitive types (int, str, etc.) as-is

def compare_json(json1, json2):
    """Compare two JSON objects, with key order and list order flexibility."""
    json1_normalized = normalize_json(json1)
    json2_normalized = normalize_json(json2)
    return json1_normalized == json2_normalized

def partial_compare(json1, json2):
    """Check if json1 has all the required keys and values from json2."""
    if isinstance(json1, dict) and isinstance(json2, dict):
        for key, value in json2.items():
            if key not in json1 or not compare_json(json1[key], value):
                return False
        return True
    return compare_json(json1, json2)

def extract_complexity(file_name):
    """Extract the level of complexity from the file name."""
    # Assuming the file pattern is <running_number>_<complexity>.json or <running_number>_<complexity>_solution.json
    parts = file_name.split('_')
    if len(parts) > 1:
        complexity = parts[1].replace('.json', '')  # Extract the complexity part
    else:
        complexity = "unknown"  # Default if the pattern is wrong
    return complexity

def main(directory, csv_output):
    results = []

    # Path to the solutions folder (one folder up)
    solutions_folder = os.path.join(os.path.dirname(directory), '../solutions')

    # List all files in the directory
    files = sorted(f for f in os.listdir(directory) if f.endswith('.json') and not f.endswith('_solution.json'))

    for json_file in files:
        # Get corresponding solution file from the "solutions" folder
        solution_file = json_file.replace('.json', '_solution.json')
        solution_path = os.path.join(solutions_folder, solution_file)

        json_path = os.path.join(directory, json_file)

        # Extract the level of complexity from the file name
        complexity_level = extract_complexity(json_file)

        # Initialize result entry
        result = {"file": json_file, "complexity": complexity_level, "result": "Failed", "reason": ""}

        # Check if the first file is a valid JSON
        if not is_valid_json(json_path):
            result["reason"] = "Invalid JSON format"
            results.append(result)
            continue

        # Check if the solution file exists
        if not os.path.exists(solution_path):
            result["reason"] = "Solution file not found"
            results.append(result)
            continue

        # Load the JSON files
        json_data = load_json(json_path)
        solution_data = load_json(solution_path)

        # First, try a normalized comparison
        if compare_json(json_data, solution_data):
            result["result"] = "Success"
            result["reason"] = "Match (with normalized comparison)"
        # If direct comparison fails, try partial matching
        elif partial_compare(json_data, solution_data):
            result["result"] = "Success"
            result["reason"] = "Partial match (required keys and values present)"
        else:
            result["reason"] = "Key/Value mismatch"

        results.append(result)

    # Write results to CSV
    with open(csv_output, mode='w', newline='') as csv_file:
        fieldnames = ['file', 'complexity', 'result', 'reason']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in results:
            writer.writerow(row)

    print(f"Results saved to {csv_output}")

if __name__ == "__main__":
    directory = "./result_files"  # The directory where the JSON files are located (modify if needed)
    csv_output = "test_results.csv"  # Change the CSV file path if needed
    main(directory, csv_output)
