Here's an exercise instruction for the given JSON object:

# Modify and Extend a Product Availability JSON Object

## Objective:
The goal of this exercise is to modify and extend a product availability JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing the availability date for a product.
Your tasks are as follows:

1. Add a new property: Add a new property called "productDescription" to the JSON. The "productDescription" should contain the following fields:
    - "brand": "Brand X"
    - "modelNumber": "ABC123"
    - "features": ["4K resolution", "HDR support"]
2. Modify an existing property: Update the "availabilityStatus" to reflect a change in inventory levels. Set it to "out of stock".
3. Add a new store location: Add another store location for this product by duplicating the existing "store" object and updating its details:
    - Change the "storeName" to "CostCo"
    - Update the "storeLocation" accordingly
4. Remove a property: Remove the "estimatedShipDate" property from the JSON object.
5. Restructure the data: Move the "quantityAvailable" field into a nested object called "inventory" with the structure:
```
json
"inventory": {
    "quantityAvailable": 10,
    "unitsInStock": 50,
    "reorderThreshold": 20
}
```