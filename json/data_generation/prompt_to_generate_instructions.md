You are a programming teacher and instructor. You help me to create exercises for my students.
I need an exercise where the students are tasked to manipulate/modify a JSON file. This can be modifying the structure or the content. 
It is very important, that the instructions are clear, concise, unambiguous and deterministic. There should not be any optional or bonus tasks that could lead to any varying outcomes.
I will provide you with the JSON.
Your task is to come up with an enganging exercise in natural language that suits the given JSON and creativly variate the task steps. Create 3-5 steps.

I give you 2 examples of good answers:

<EXAMPLES>

    <INPUT JSON>
        {
            "id": 1,
            "name": "John Doe",
            "age": 28,
            "email": "john.doe@example.com"
        }
    </INPUT JSON>



    <OUTPUT instruction>
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

    </OUTPUT instruction>
    
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

    <OUTPUT instruction>
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

    </OUTPUT instruction>


</EXAMPLES>

The Output will be directly parsed into an .md file, so please make sure to follow the markdown syntax.
Alright, now it's your turn! Please create a new exercise instruction.md based on the given JSON object. 

{{json_content}}