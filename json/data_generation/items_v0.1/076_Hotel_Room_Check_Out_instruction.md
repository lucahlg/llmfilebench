Here's an exercise instruction based on the given JSON object:

# Modify and Extend a Hotel Checkout Information JSON Object

## Objective:
The goal of this exercise is to modify and extend a hotel checkout information JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a guest's hotel checkout information.
Your tasks are as follows:

1. Add a new property called "paymentMethod" to the JSON object. The "paymentMethod" should contain the following fields:
    - "type": "Credit Card"
    - "cardNumber": "1234-5678-9012-3456"    
    - "expirationDate": "2025-12-31"

2. Update an existing property: The guest has changed their mind about the room type and now prefers a single bed. Update the "roomType" in the "room" object to reflect this change.

3. Remove a property: Remove the "note" field from the JSON object, as it's no longer relevant.

4. Restructure the data: Move the "firstName", "lastName", and "email" fields into a nested object called "guestInfo" with the structure:
```
    "guestInfo": {
        "id": 12345,
        "name": {
            "first_name": "Jane",
            "last_name": "Doe"
        },
        "contact": {
            "email": "jane.doe@example.com"
        }
    }
```