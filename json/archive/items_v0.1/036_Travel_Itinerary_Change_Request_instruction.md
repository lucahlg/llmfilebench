Here's an exercise instruction for you:

# Modify and Extend a Traveler's Flight Change Request JSON Object

## Objective:
The goal of this exercise is to modify and extend a traveler's flight change request JSON object by adding new properties, updating existing values, and reorganizing the structure.

## Exercise Instructions:

You are provided with a JSON file representing a traveler's flight change request. Your tasks are as follows:

1. Add a new property called "specialRequests" to the JSON object. The "specialRequests" object should contain the following:
    - "mealPreference": "Vegetarian"
    - "seatPreferance": "Window seat, if available"
2. Update the "changeType" from "Flight" to "Hotel" and change the flight-related fields ("flightNumber", "newDepartureDate", etc.) to hotel-related fields:
    - "hotelName": "Grand Hotel Downtown"
    - "checkInDate": "2023-08-16"
    - "checkOutDate": "2023-08-17"
3. Add a new property called "travelerType" to the JSON object. The "travelerType" should be set to "Business".
4. Modify the "reasonForChange" field to better reflect the updated change type (now Hotel instead of Flight). Your change must still explain why the traveler wants to make this request.
5. Remove the "additionalNotes" property from the JSON object.

Note: The "travelerInfo" section should remain unchanged throughout this exercise.