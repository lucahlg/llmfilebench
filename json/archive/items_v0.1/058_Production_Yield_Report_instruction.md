Here's an exercise instruction based on the given JSON object:

# Modify and Analyze a Chocolate Production Process JSON Object

## Objective:
The goal of this exercise is to modify and analyze a chocolate production process JSON object by adding new properties, updating existing values, reorganizing the structure, and calculating derived values.

## Exercise Instructions:
You are provided with a JSON file representing a chocolate production process. Your tasks are as follows:

1. Add a new raw material: Add a new item to the "rawMaterials" array with the following details:
    - name: "Milk Powder"
    - quantity: 30
    - unit: "KG"
2. Update the production steps: The duration of the "Grinding Cocoa Beans" step has been increased by 15 minutes. Update the "duration" field for this step.
3. Add a new property to the product object: Include the following fields in the "product" object:
    - "category": "Confectionery"
    - "shelfLife": "6 months"
4. Calculate and add derived values: Calculate the total cost of raw materials used in the production process by multiplying each raw material's quantity by its assumed cost per unit (e.g., Cocoa Beans: $10/KG, Sugar: $5/KG, etc.). Add a new field called "totalRawMaterialCost" to the JSON object with this calculated value.
5. Restructure the data: Move the "productionSteps" array into a nested object called "productionProcess" with the structure:
```json
{
    "productionDate": "2023-03-08",
    "product": {
        // ...
    },
    "rawMaterials": [
        // ...
    ],
    "productionProcess": {
        "steps": [
            // ...
        ]
    }
}
```
Note: Assume the cost per unit for each raw material is as follows:
* Cocoa Beans: $10/KG
* Sugar: $5/KG
* Butter: $15/KG
* Milk Powder: $8/KG