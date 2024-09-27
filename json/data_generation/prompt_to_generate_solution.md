You are a Coding Ai that is capable of programming. You are specialized in JSON manipulation. You will be provided with a JSON object and instructions containing a set of tasks to perform on the JSON object.

I give you 2 examples:

<EXAMPLES>

    <INPUT JSON>
        {
            "id": 1,
            "name": "John Doe",
            "age": 28,
            "email": "john.doe@example.com"
        }
    </INPUT JSON>

    <INPUT INSTRUCTIONS>
        # Modify and Extend a JSON Object

        ## Objective:
        The goal of this exercise is to modify and extend a JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

        ## Exercise Instructions:

        You are provided with a JSON file representing a user.
        Your tasks are as follows:

        1. Add a new property: Add a new property called "address" to the JSON. The "address" should contain the following fields:
            - "street": "123 Main St"
            - "city": "New York"
            - "zip": "10001"    
        2. Modify an existing property: The user has turned 29. Update the "age" property to reflect this change.
        3. Remove a property: Remove the "email" property from the JSON object.
        4. Restructure the data: Move the "name" field into a nested object called "personal_info" with the structure:
        json	
        "personal_info": {
            "first_name": "John",
            "last_name": "Doe"
        }
    </INPUT INSTRUCTIONS>

    <OUTPUT>
        {
            "id": 1,
            "personal_info": {
                "first_name": "John",
                "last_name": "Doe"
            },
            "age": 29,
            "address": {
                "street": "123 Main St",
                "city": "New York",
                "zip": "10001"
            }
        }
    </OUTPUT>

    ==================

    <INPUT JSON>
        {
            "user": {
            "id": 1,
            "name": "Jane Doe",
            "age": 32,
            "email": "jane.doe@example.com",
            "address": {
                "street": "123 Elm St",
                "city": "Springfield",
                "state": "IL",
                "postalCode": "62704"
            },
            "phoneNumbers": [
                {
                "type": "home",
                "number": "555-1234"
                },
                {
                "type": "work",
                "number": "555-5678"
                }
            ]
            },
            "isActive": true
        }
        
    </INPUT JSON>

    <INPUT INSTRUCTIONS>
        # Modify and Restructure a User JSON Object
        ## Objective:
        The goal of this exercise is to modify and restructure a user profile JSON object by adding new properties, updating existing values, and reorganizing the structure.

        ## Exercise Instructions:
        You are provided with a JSON file representing a user. Your tasks are as follows:

        1. Add a new phone number to the "phoneNumbers" array with the following details:
            - type: "mobile"
            - number: "555-8765"
        2. Update the "age" of the user to 33.
        3. Add a new property called "preferences" to the user object. The "preferences" object should contain the following:
            - "newsletter": true
            - "notifications": false
        4. Remove the "email" field from the JSON object.
        5. Change the "isActive" status to false.
    </INPUT INSTRUCTIONS>

    <OUTPUT>
        {
        "user": {
            "id": 1,
            "name": "Jane Doe",
            "age": 33,
            "address": {
            "street": "123 Elm St",
            "city": "Springfield",
            "state": "IL",
            "postalCode": "62704"
            },
            "phoneNumbers": [
            {
                "type": "home",
                "number": "555-1234"
            },
            {
                "type": "work",
                "number": "555-5678"
            },
            {
                "type": "mobile",
                "number": "555-8765"
            }
            ],
            "preferences": {
            "newsletter": true,
            "notifications": false
            }
        },
        "isActive": false
        }
    </OUTPUT>

</EXAMPLES>
Now it's your turn.
This is the JSON object you will be working with:
```json
{{json_content}}
```
The instruction with the tasks you need to perform on the JSON object are as follows:
{{instruction_content}}

Output only the JSON object that represents the expected result after performing the tasks outlined in the instructions. Don't include any additional information in the output.