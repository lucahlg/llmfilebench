Here's an exercise instruction based on the given JSON object:

# Modify and Enhance a Patient Profile JSON Object

## Objective:
The goal of this exercise is to modify and enhance a patient profile JSON object by adding new fields, updating existing values, removing unnecessary information, and reorganizing the structure.

## Exercise Instructions:

You are provided with a JSON file representing a patient's medical history. Your tasks are as follows:

1. Add a new field called "emergencyContact" to the JSON object. The "emergencyContact" should contain the following details:
	* name: John Doe
	* phone number: 555-1234
2. Update the patient's date of birth to "1985-01-01".
3. Remove the "gender" field from the JSON object as it is not relevant in this context.
4. Add a new medical diagnosis to the "diagnoses" array with the following details:
	* code: "I50"
	* description: "Coronary artery disease"
5. Move the "medications" and "immunizations" arrays into a nested object called "medicalHistory" with the following structure:

json	
"medicalHistory": {
    "medications": [...],
    "immunizations": [...]
}
6. Change the "severity" of the allergy to Sulfa drugs from "Moderate" to "Severe".

Note: Be sure to follow proper JSON syntax and formatting guidelines while performing these modifications.