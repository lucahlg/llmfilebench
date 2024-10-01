
# Modify and Extend a JSON Object

## Objective:
The goal of this exercise is to modify and extend a JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a course.
Your tasks are as follows:

1. Add a new property: Add a new property called "semester" to the course object. The "semester" should contain the following fields:
    - "term": "Fall"
    - "year": 2024
2. Modify an existing property: The course has been updated to give 4 credits. Update the "credits" property accordingly.
3. Remove a property: Remove the "isFull" property from the JSON object.
4. Restructure the data: Move the "instructor" field into a nested object under "staff" with the structure:
```json
"staff": {
    "instructor": {
        "firstName": "Emily",
        "lastName": "Clark",
        "email": "e.clark@university.edu"
    }
}
```
