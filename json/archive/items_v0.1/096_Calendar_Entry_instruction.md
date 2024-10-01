Based on the provided JSON object, here's a new exercise instruction with 5 steps:

# Modify and Enhance a Meeting Event JSON Object

## Objective:
The goal of this exercise is to modify and enhance a meeting event JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a team meeting.
Your tasks are as follows:

1. **Add Recurring Details**: Add a new property called "recurringDetails" to the JSON object. The "recurringDetails" should contain the following:
    - "endTime": "2023-03-15T11:00:00-07:00"
    - "endDate": "2023-04-01"
2. **Update Event Details**: Update the "summary" property to reflect a new topic: "Discuss Project Progress".
3. **Modify Location Information**: Update the "location.displayName" to "Googleplex, Mountain View Campus" and add a new field called "floorNumber" with value "3".
4. **Restructure Attendees Array**: Move each attendee's details into a separate object within the "attendees" array. For example:
    - "email": "alice@example.com"
    - "displayName": "Alice Smith"
    - "status": "accepted"
5. **Remove Redundant Information**: Remove the "self" field from all attendees and update the "reminders" array to contain only one reminder with method "popup".

Your task is to modify the provided JSON object according to these instructions, demonstrating your ability to manipulate and enhance a complex JSON structure.