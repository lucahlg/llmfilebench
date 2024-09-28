Here's a new exercise instruction based on the given JSON object:

# Modify and Extend a Flight Passenger JSON Object

## Objective:
The goal of this exercise is to modify and extend the JSON object representing a flight passenger by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a flight passenger.
Your tasks are as follows:

1. **Add additional flight details**: Add a new property called "traveler" to the passenger object within the "header". The "traveler" should contain the following fields:
    - "type": "business"
    - "fare": "$500.00"
2. **Update boarding time**: Update the "boardingTime" field under the "header" to "14:30".
3. **Remove unneeded flight information**: Remove the "flights" array from the JSON object, as it is not relevant to the passenger's profile.
4. **Reorganize notes and add new field**: Move the "notes" field into a nested object called "flight_info". Additionally, update the "notes" value to include an additional instruction: "...and do not forget your passport!"
5. **Add new personal details**: Add a new property called "personal_details" under the "header". The "personal_details" should contain the following fields:
    - "passportNumber": (remove this field from the "passenger" object and add it here)
    - "emergencyContactName": "Samantha Smith"
    - "emergencyContactPhone": "555-1234"

This exercise will test your students' ability to modify, extend, and restructure JSON objects, while also ensuring they understand the importance of data organization and formatting.