Here's an exercise instruction for the given JSON object:

# Modify and Extend a Shopping Order JSON Object

## Objective:
The goal of this exercise is to modify and extend a shopping order JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a completed shopping order.
Your tasks are as follows:

1. Add new items: Add two new products to the "items" array. The new products should have the following details:
	* Product 1: Apple AirPods Pro ( price = $249.99, quantity = 3)
	* Product 2: Amazon Echo Dot (price = $49.99, quantity = 4)
2. Update a product's description: Update the description of the "Samsung Galaxy S22 Ultra" to include information about its charging speed and battery life.
3. Remove a field from an address: Remove the "state" field from both the shippingAddress and billingAddress objects.
4. Add a new property to the order object: Add a new property called "discountApplied" to the order object, and set it to true if the subtotal is greater than $2000.
5. Calculate a new total: Recalculate the total price of the order by including the discount, if applicable.

## Hints:

* When adding new items, remember to include their respective product details (name, description, price) and quantity.
* When updating a product's description, make sure to keep the existing information intact.
* When removing fields from addresses, only remove the "state" field, leaving the other address details unchanged.

## Example Expected Output:
Your final JSON output should have the modified order object with the new items, updated product descriptions, and removed fields, as well as the recalculated total price.