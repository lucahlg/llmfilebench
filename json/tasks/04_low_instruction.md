
# Modify and Extend a JSON Object

## Objective:
The goal of this exercise is to modify and extend a JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a user.
Your tasks are as follows:

1. Add a new property: Add a new property called "contact_details" to the JSON. The "contact_details" should contain the following fields:
    - "phone": "555-1234"
    - "alternate_email": "alice.alt@example.com"    
2. Modify an existing property: The user has turned 25. Update the "age" property to reflect this change.
3. Remove a property: Remove the "email" property from the JSON object.
4. Restructure the data: Move the "name" field into a nested object called "personal_details" with the structure:
```json	
"personal_details": {
    "first_name": "Alice",
    "last_name": "Smith"
}
```
