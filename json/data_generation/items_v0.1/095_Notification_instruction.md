Here's an exercise instruction for the given JSON object:

# Manipulate and Extend a Message JSON Object

## Objective:
The goal of this exercise is to modify and extend a message JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a message.
Your tasks are as follows:

1. **Update Message Status**: Update the "status" property from "new" to "read".
2. **Add Recipient Details**: Add two new properties called "phoneNumbers" and "address" to the "recipient" object. The "phoneNumbers" should be an array containing:
    - A phone number of type "home" with number "555-1234"
    - A phone number of type "work" with number "555-5678"
The "address" property should contain:
    - Street: "456 Maple St"
    - City: "Anytown"
    - State: "CA"
3. **Modify Message Details**: Update the "title" and "body" properties of the message object. The new title should be "New Message from John Smith (Updated)" and the body should contain the following text:
    "Hi Jane, I hope you're having a great day! I wanted to let you know that I've updated the original message. Please check your inbox for more details."
4. **Remove Unnecessary Fields**: Remove the "updated_at" property from the JSON object.
5. **Restructure Message Properties**: Move the "title" and "body" properties into a nested object called "message_details". The resulting structure should look like this:
```
{
    ...
    "message": {
        "id": "...",
        "message_details": {
            "title": "...",
            "body": "..."
        }
    }
}
```