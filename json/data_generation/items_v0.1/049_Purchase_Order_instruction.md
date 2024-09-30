Here's an exercise instruction based on the given JSON object:

# Modify and Extend a Purchase Order JSON Object

## Objective:
The goal of this exercise is to modify and extend a purchase order JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing an order from Acme Corporation.
Your tasks are as follows:

1. Add new tax information: Add a new property called "taxInformation" to the JSON object. The "taxInformation" should contain the following fields:
	* "taxRate": 8
	* "taxAmount": 24.0
2. Update the delivery date: Change the "deliveryDate" to "2023-03-22T12:00:00Z".
3. Modify an item quantity: The supplier has informed you that they can only supply 5 units of "ITEM9876543210". Update the "quantity" field for this item in the JSON.
4. Add a new item to the order: Insert a new item into the "items" array with the following details:
	* itemId: "ITEM5551234567"
	* quantity: 15
	* unitPrice: 50.0
5. Restructure the supplier information: Move the entire "supplier" object into a nested property called "vendorDetails".

Note: Make sure to keep track of any changes made to the original JSON structure and values!