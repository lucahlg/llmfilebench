# Modify and Extend a Meeting JSON Object

## Objective:
The goal of this exercise is to modify and extend a meeting JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a meeting.
Your tasks are as follows:

1. **Add recurring meeting details**: Add a new property called "recurring" to the JSON. The "recurring" object should contain the following:
    - "frequency": "weekly"
    - "endDate": "2023-05-08T11:00:00Z"
2. **Update location information**: Update the "location" object to include the conference room capacity and a nearby landmark.
    - "capacity": 50
    - "landmark": "Anytown City Hall"
3. **Modify attendee list**: Remove Bob Jones from the attendees array and add two new attendees:
    - "name": "David Lee",
    "email": "david.lee@example.com"
    - "name": "Emily Chen",
    "email": "emily.chen@example.com"
4. **Remove reminders for mobile devices**: Update the reminders array to only include reminders sent via email or pop-up, removing any reminders with a method of "sms" or "text message".
5. **Restructure attendee data**: Move the "name" and "email" fields into a nested object called "attendee_info" within each attendee JSON object.

```json
{
    "id": "01234567-89ab-cdef-0123-456789abcdef",
    "title": "Engineering Team Meeting",
    "description": "Discuss the latest project updates and plan for the upcoming sprint.",
    "startTime": "2023-03-08T10:00:00Z",
    "endTime": "2023-03-08T11:00:00Z",
    "location": {
        "name": "Conference Room A",
        "address": "123 Main Street, Anytown, CA 91234",
        "capacity": 50,
        "landmark": "Anytown City Hall"
    },
    "recurring": {
        "frequency": "weekly",
        "endDate": "2023-05-08T11:00:00Z"
    },
    "attendees": [
        {
            "attendee_info": {
                "name": "Alice Smith",
                "email": "alice.smith@example.com"
            }
        },
        {
            "attendee_info": {
                "name": "Carol Green",
                "email": "carol.green@example.com"
            }
        },
        {
            "attendee_info": {
                "name": "David Lee",
                "email": "david.lee@example.com"
            }
        },
        {
            "attendee_info": {
                "name": "Emily Chen",
                "email": "emily.chen@example.com"
            }
        }
    ],
    "reminders": [
        {
            "time": "2023-03-08T09:30:00Z",
            "method": "email"
        },
        {
            "time": "2023-03-08T09:45:00Z",
            "method": "popup"
        }
    ]
}
```