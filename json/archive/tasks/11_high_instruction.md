
# Modify and Extend a JSON Object

## Objective:
The goal of this exercise is to modify and extend a JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a library.
Your tasks are as follows:

1. Add a new property: Add a new property called "libraryDirector" to the library object. The "libraryDirector" should contain the following fields:
    - "name": "Dr. Amanda Lewis"
    - "since": "2019-07-01"
2. Modify an existing property: One of the books has been fully borrowed. Update the "availableCopies" of the book with bookId 2001 to 0.
3. Remove a property: Remove the "email" field from the member with "memberId" 3001 in the members list.
4. Restructure the data: Move the "address" object into a new nested object called "location" inside the "library" object. It should have the following structure:
```json
"location": {
    "address": {
        "street": "456 Library Lane",
        "city": "Central City",
        "state": "CA",
        "postalCode": "90002",
        "country": "USA"
    }
}
```
