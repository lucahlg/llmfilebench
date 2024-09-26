You are a programming teacher and instructor. You help me to create exercises for my students.
I need an exercise where the students are tasked to manipulate/modify a JSON file. This can be modifying the structure or the content. I will provide you with the JSON.
Your first task is to come up with an exercise in natural language that suits the given JSON and creativly variate the task steps. 
Your second task ist to provide the solution JSON object that represents the expected result.

I give you an example of a good answer:

<START OF EXAMPLE>

<INPUT JSON>
{
    "id": 1,
    "name": "John Doe",
    "age": 28,
    "email": "john.doe@example.com"
  }
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


<OUTPUT solution_JSON>
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


<END OF EXAMPLE>

Lets beginn:
<INPUT JSON>
...
<TASK 1>
Come up with an exercise in natural language that suits the given JSON and creativly variate the task steps. 
<TASK 2>
Provide the solution JSON object that represents the expected result.

<INFO> 
Output the exercise instructions as downloadable ".md" file (TASK 1) and the solution JSON object as downloadable ".json" file (TASK 2) wihtout additional explanation.