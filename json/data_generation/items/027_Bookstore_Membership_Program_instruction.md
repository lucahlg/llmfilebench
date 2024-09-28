# Modify and Extend a Loyalty Program JSON Object

## Objective:
The goal of this exercise is to modify and extend a loyalty program's configuration by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a loyalty program.
Your tasks are as follows:

1. **Add a new tier**: Create a new "tier" object called "Platinum" with an ID of 4 and a discount of 0.25. Add this new tier to the end of the existing tiers list.
2. **Update membership details**: Update the email address of Alice Smith (membership ID 1) to "alice.smith.new@example.com". Also, update her start date to January 1st, 2024, and end date to December 31st, 2025.
3. **Modify a tier's discount**: Decrease the discount for the Silver tier by 0.01 (making it 0.14).
4. **Add a new property to memberships**: For each membership, add a new object called "loyalty_history" with an empty array of transactions. Update this field in all existing memberships.
5. **Change the status of a membership**: Change the status of Bob Jones' membership (membership ID 2) from inactive to active.

Note: You should manipulate the JSON data according to these instructions, without changing any other part of it, and make sure your code is properly formatted and follows best practices for coding style.