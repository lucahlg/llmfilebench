Here's an exercise instruction based on the given JSON object:

# Modify and Enhance Hazardous Material Handling Instructions

## Objective:
The goal of this exercise is to modify and enhance hazard handling instructions by adding, updating, and removing properties. You will also be asked to restructure part of the instructions.

## Exercise Instructions:

You are provided with a JSON file representing hazardous material handling instructions.
Your tasks are as follows:

1. **Add a new condition**: Add a new "storage_conditions" to the JSON object that includes:
    - "Avoid direct sunlight"
    - "Protect from contamination"
2. **Update an existing property**: Update the "handling_code" to reflect a higher level of caution ("C").
3. **Create a nested object**: Move the "special_handling_instructions" into a nested object called "safety_precautions" with the structure:
```
"safety_precautions": {
    "keep_away_from": ["heat", "moisture"],
    "additional_steps": "Take extra precautions when handling."
}
```
4. **Remove unnecessary data**: Remove the redundant storage condition from the original array.
5. **Reorganize the structure**: Move the "handling_description" to a nested object called "general_handling_instructions" with the same content, and keep it as a top-level property.

Your task is to update the JSON object according to these instructions. Show your code snippet that demonstrates each step, and include any necessary comments or explanations.