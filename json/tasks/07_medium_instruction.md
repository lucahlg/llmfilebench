
# Modify and Extend a JSON Object

## Objective:
The goal of this exercise is to modify and extend a JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a product.
Your tasks are as follows:

1. Add a new property: Add a new property called "manufacturer" to the product object. The "manufacturer" should contain the following fields:
    - "name": "TechCorp"
    - "country": "USA"
2. Modify an existing property: The price of the product has been reduced. Update the "price" property to reflect a new price of 24.99.
3. Remove a property: Remove the "inStock" property from the product object.
4. Restructure the data: Move the "dimensions" field into a nested object called "specifications" inside the "product" object. It should have the following structure:
```json
"specifications": {
    "dimensions": {
        "length": 4.5,
        "width": 2.3,
        "height": 1.5
    }
}
```
