Here's an exercise instruction for the given JSON object:

**# Parse and Modify a SMS Message JSON Object**

## **Objective**
The goal of this exercise is to parse and modify a JSON object representing an SMS message by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## **Exercise Instructions:**

You are provided with a JSON file representing an SMS message.
Your tasks are as follows:

1. **Add sender information**: Add a new property called "sender_info" to the JSON object. The "sender_info" should contain the following fields:
    - "name": "John Doe"
    - "location": "New York"
2. **Update message content**: Update the "body" property to include an additional sentence: "I'm doing great, thanks!"
3. **Change status**: Update the "status" property to "DELIVERED".
4. **Restructure timestamp**: Move the "sentAt" field into a nested object called "timestamp_info" with the structure:
    ```json
    {
        "date": "2023-03-08",
        "time": "18:30"
    }
```
5. **Remove redundant information**: Remove the unnecessary fields from the JSON object.

Note: This exercise focuses on manipulating and restructuring the given JSON object, rather than creating a new one from scratch. Students will need to use their JSON parsing and modification skills to complete the tasks!