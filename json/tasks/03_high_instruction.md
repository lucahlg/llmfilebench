# Modify and Update an Order JSON Object
## Objective:
The goal of this exercise is to modify and restructure the given order JSON object by adding new properties, updating values, and removing unnecessary fields. You will also be asked to restructure a part of the JSON.

## Exercise Instructions:
You are provided with a JSON file representing a customer order. Your tasks are as follows:

1. Add a new item to the "items" array: Add a product with the following details:
    - productId: 103
    - name: "Keyboard"
    - quantity: 1
    - price: 45.00
    - discount: 5% (percentage)
2. Update the customer's "phone" number to "555-1234".
3. Remove the "billing" address from the "addresses" array.
4. Update the "payment" method to "paypal" and remove the "transactionId" field.
5. Modify the "totalAmount" to reflect the new total amount including the new item and updated discounts, assuming the new total is $992.23.