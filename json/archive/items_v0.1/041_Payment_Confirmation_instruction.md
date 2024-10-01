Here is a new exercise instruction based on the given JSON object:

# Modify and Extend an Order JSON Object

## Objective:
The goal of this exercise is to modify and extend a JSON object representing an order by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing an order.
Your tasks are as follows:

1. Add a new product: Add a new product called "Apple AirPods Pro" to the "products" array. The product should have the following details:
    - name: "Apple AirPods Pro"
    - unitPrice:
        - value: 249.0
        - currencyCode: "USD"
    - quantity:
        - amount: 2
        - unit: "PAIRS"

2. Update a discount: The store is running a promotion and wants to increase the discount by $25. Update the "discount" object to reflect this change.

3. Remove a property: Remove the "customerEmail" field from the JSON object.

4. Restructure the data: Move the "customerName", "customerAddress", and "status" fields into a nested object called "orderInfo" with the structure:

    json
    "orderInfo": {
        "customerName": "John Smith",
        "customerAddress": "123 Main Street, Anytown, CA 12345",
        "status": "CONFIRMED"
    }

5. (Optional) Add a new property to the order: Add a new field called "shippingDate" with the date of shipping. Make sure to handle the case where this field is not present in the original JSON.

Note: Depending on your preference, you can make the last step optional or require it as part of the exercise.