
# Modify and Extend a JSON Object

## Objective:
The goal of this exercise is to modify and extend a JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a user.
Your tasks are as follows:

1. Add a new property: Add a new property called "social_media" to the JSON. The "social_media" should contain the following fields:
    - "twitter": "@charlie_davis"
    - "linkedin": "linkedin.com/in/charliedavis"
2. Modify an existing property: The user has turned 30. Update the "age" property to reflect this change.
3. Remove a property: Remove the "email" property from the JSON object.
4. Restructure the data: Move the "name" field into a nested object called "personal_data" with the structure:
```json	
"personal_data": {
    "first_name": "Charlie",
    "last_name": "Davis"
}
```
