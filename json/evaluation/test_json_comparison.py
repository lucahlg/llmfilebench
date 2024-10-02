import os
import json
import csv
from datetime import datetime

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
        # Sort lists after normalizing each element
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
            if key not in json1 or not partial_compare(json1[key], value):
                return False
        return True
    elif isinstance(json1, list) and isinstance(json2, list):
        # Check if all items in json2 are in json1
        for item in json2:
            if not any(partial_compare(elem, item) for elem in json1):
                return False
        return True
    else:
        return json1 == json2

def calculate_complexity(data):
    """Calculate the complexity of a JSON object."""
    def traverse(node, depth=0):
        nonlocal max_depth, total_elements, max_breadth
        if isinstance(node, dict):
            total_elements += len(node)
            max_breadth = max(max_breadth, len(node))
            max_depth = max(max_depth, depth)
            for value in node.values():
                traverse(value, depth + 1)
        elif isinstance(node, list):
            total_elements += len(node)
            max_breadth = max(max_breadth, len(node))
            max_depth = max(max_depth, depth)
            for item in node:
                traverse(item, depth + 1)
        else:
            total_elements += 1
            max_depth = max(max_depth, depth)

    max_depth = 0
    total_elements = 0
    max_breadth = 0
    traverse(data)

    # Define thresholds for complexity levels
    if max_depth <= 3 and total_elements <= 10:
        complexity_level = "Low"
    elif max_depth <= 6 and total_elements <= 50:
        complexity_level = "Medium"
    else:
        complexity_level = "High"

    return {
        "max_depth": max_depth,
        "total_elements": total_elements,
        "max_breadth": max_breadth,
        "complexity_level": complexity_level
    }

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

        # Initialize result entry
        result = {"file": json_file, "result": "Failed", "reason": "", "complexity": ""}

        # Check if the first file is a valid JSON
        if not is_valid_json(json_path):
            result["reason"] = "Invalid JSON format"
            results.append(result)
            continue

        # Load the JSON data
        json_data = load_json(json_path)

        # Calculate complexity of the JSON data
        complexity_info = calculate_complexity(json_data)
        result["complexity"] = complexity_info["complexity_level"]

        # Check if the solution file exists
        if not os.path.exists(solution_path):
            result["reason"] = "Solution file not found"
            results.append(result)
            continue

        # Load the solution data
        solution_data = load_json(solution_path)

        # First, try a normalized comparison
        if compare_json(json_data, solution_data):
            result["result"] = "Success"
            result["reason"] = "Exact match (with normalized comparison)"
        # If direct comparison fails, try partial matching
        elif partial_compare(json_data, solution_data):
            result["result"] = "Success"
            result["reason"] = "Partial match (required keys and values present)"
        else:
            result["reason"] = "Key/Value mismatch"

        results.append(result)

    # Write results to CSV
    with open(csv_output, mode='w', newline='') as csv_file:
        fieldnames = ['file', 'result', 'reason', 'complexity']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in results:
            writer.writerow(row)

    print(f"Results saved to {csv_output}")

if __name__ == "__main__":
    directory = "./result_files"  # The directory where the JSON files are located (modify if needed)
    # Generate a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_output = f"test_results_{timestamp}.csv"  # Change the CSV file path if needed
    main(directory, csv_output)
