# Upgrade Flight Request JSON Modification Exercise

## Objective:
The goal of this exercise is to modify a flight upgrade request JSON object by updating, adding, and removing properties.

## Exercise Instructions:

You are provided with a JSON file representing a flight upgrade request. Your tasks are as follows:

1. **Update passenger information**: The passenger has changed their email address. Update the "email" field in the "passenger" object to reflect this change.
2. **Add new request details**: Add a new property called "requestedServiceClass" to the JSON object, with the value set to "Priority Check-in".
3. **Update upgrade reason**: The passenger wants to provide more context for their upgrade request. Update the "upgradeReason" field to include an additional sentence: "I am celebrating my anniversary and I would like to make it special."
4. **Remove unnecessary status update**: Remove the "status" property from the JSON object, as this information is not relevant to the passenger's flight upgrade request.
5. **Restructure the flight segment data**: Move the "flightNumber" field into a separate object called "flightInformation", with the structure:
json
"flightInformation": {
    "carrier": "AA",
    "flightNumber": 1234
}

Note: Your modified JSON should still maintain its overall structure and hierarchy, but with the requested changes.