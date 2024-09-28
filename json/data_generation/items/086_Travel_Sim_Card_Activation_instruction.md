Here's an exercise instruction for the given JSON object:

# Modify and Extend a Mobile User JSON Object

## Objective:
The goal of this exercise is to modify and extend a JSON object representing a mobile user by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a mobile user.
Your tasks are as follows:

1. **Add historical data**: Add two new call history records to the "callHistory" array with the following details:
    - `destination`: "+1-111-222-3333"
    - `duration`: 1200
    - `callDate`: "2023-03-11"
    
2. **Update customer information**: Update the "name" and "email" fields of the "customer" object to reflect a change in contact details.
    
3. **Modify data usage**: Increase the "dataUsage" value by 1024 bytes.
    
4. **Reorganize the JSON structure**: Move the "activationDate" field into the nested "customer" object, creating a new "personal_info" object with the following structure:
    ```json
        "customer": {
            "customerId": "CUST-5678",
            "name": "Jane Doe",
            "email": "jane.doe@example.com",
            "personal_info": {
                "date_of_birth": "1990-01-01"
            }
        }
    ```
    
5. **Change activation status**: Update the "activationStatus" field to reflect a new status of "INACTIVE".