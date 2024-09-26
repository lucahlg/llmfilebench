
# Modify and Extend a JSON Object

## Objective:
The goal of this exercise is to modify and extend a JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a vehicle.
Your tasks are as follows:

1. Add a new property: Add a new property called "owner" to the vehicle object. The "owner" should contain the following fields:
    - "name": "Michael Turner"
    - "licenseNumber": "A1234567"
2. Modify an existing property: The vehicle has a new feature. Add "Heated Seats" to the "features" array.
3. Remove a property: Remove the "isAvailable" property from the JSON object.
4. Restructure the data: Move the "specs" field into a nested object called "details" inside the "vehicle" object. It should have the following structure:
```json
"details": {
    "specs": {
        "engine": "2.5L",
        "horsepower": 203,
        "fuelType": "Gasoline"
    }
}
```
