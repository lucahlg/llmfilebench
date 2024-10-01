
# Modify and Extend a JSON Object

## Objective:
The goal of this exercise is to modify and extend a JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing an e-commerce transaction.
Your tasks are as follows:

1. Add a new property: Add a new property called "deliveryInstructions" to the "shipping" object. The "deliveryInstructions" should contain the following details:
    - "leaveAtDoor": true
    - "instructions": "Please leave the package at the back door."
2. Modify an existing property: The customer has received a refund for one of the items. Update the "totalPrice" of the item with "itemId" 5001 to 749.99, reducing the price by $50.
3. Remove a property: Remove the "tracking" property from the "ecommerce" object as the tracking information is unavailable.
4. Restructure the data: Move the "paymentMethod" object inside "customer" to a new nested object called "paymentDetails" with the following structure:
```json
"paymentDetails": {
    "paymentMethod": {
        "type": "Credit Card",
        "cardType": "Visa",
        "lastFourDigits": "1234",
        "expirationDate": "2025-08"
    }
}
```
