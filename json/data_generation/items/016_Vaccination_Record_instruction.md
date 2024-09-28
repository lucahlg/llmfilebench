Here's a new exercise instruction based on the given JSON object:

# Modify and Extend a Patient JSON Object

## Objective:
The goal of this exercise is to modify and extend a patient profile JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a patient's vaccination history.
Your tasks are as follows:

1. Add a new vaccination record: Add a new vaccination type called "Flu" with the following details:
    - dose: 1
    - dateAdministered: "2010-01-01"
    - lotNumber: "321654"
    - manufacturer: "Novartis"
2. Update an existing vaccination record: The patient has received a booster shot of MMR vaccine. Update the "dateAdministered" and "lotNumber" fields for the MMR vaccination.
3. Remove a vaccination type: Remove the "Chickenpox" vaccination from the list.
4. Add a new property to the patient object: Add a new field called "medicalConditions" with the following details:
    - "diabetes": false
    - "allergies": ["peanuts", "eggs"]
5. Restructure the data: Move the "dateOfBirth" field into a nested object called "personalInfo" with the structure:

json	
"personalInfo": {
    "firstName": "Jane",
    "lastName": "Doe",
    "dateOfBirth": "1990-01-01"
}