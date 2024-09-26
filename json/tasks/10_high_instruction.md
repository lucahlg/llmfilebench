
# Modify and Extend a JSON Object

## Objective:
The goal of this exercise is to modify and extend a JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing an employee.
Your tasks are as follows:

1. Add a new project: Add a new project under the "projects" array with the following details:
    - "projectId": 303
    - "name": "Project Gamma"
    - "role": "Consultant"
    - "startDate": "2024-01-15"
    - "endDate": null
2. Update the "salary" amount: The employee has received a raise. Update the "amount" field under "salary" to reflect a new salary of 90,000.
3. Remove a field: Remove the "email" field from the "contact" object.
4. Restructure the data: Move the "address" object inside "contact" to a new "location" object with the structure:
```json
"location": {
    "address": {
        "street": "321 Maple Ave",
        "city": "Metropolis",
        "state": "NY",
        "postalCode": "10001",
        "country": "USA"
    }
}
```
