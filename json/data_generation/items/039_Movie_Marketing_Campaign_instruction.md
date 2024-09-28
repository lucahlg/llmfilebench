Here's a new exercise instruction based on the given JSON object:

# Modify and Refine a Movie Campaign JSON Object

## Objective:
The goal of this exercise is to modify and refine a movie campaign JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a movie campaign.
Your tasks are as follows:

1. Add new marketing channels: Add two new objects to the "marketingChannels" array with the following details:
    - Name: "Influencer Marketing"
    - Budget: 5000000
    - Start Date: "2023-06-01"
    - End Date: "2023-08-31"
    - Name: "Event Marketing"
    - Budget: 2000000
    - Start Date: "2023-07-15"
    - End Date: "2023-09-15"

2. Update a task's status and due date: Update the "Create marketing materials" task to change its state from "In Progress" to "Completed". Also, update the due date for this task to "2023-05-25".

3. Remove a target demographic: Remove the second target demographic (the one with interests in Romance and Comedy) from the JSON object.

4. Add new budget details: Add two new properties to the root object representing additional budget allocations:
    - "Merchandise": 1500000
    - "Public Relations": 10000000

5. Restructure the tasks array: Move the "name" and "description" fields into a nested object called "task_info" with the structure:
```json
{
    "task_name": "...",
    "task_description": "..."
}
```
Make sure to preserve the original formatting of the JSON object.