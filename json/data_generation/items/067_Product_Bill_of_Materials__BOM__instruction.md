Here's an exercise instruction based on the given JSON object:

# Modify and Extend a Product Assembly JSON Object

## Objective:
The goal of this exercise is to modify and extend a product assembly JSON object by adding, updating, and removing properties, as well as reorganizing the structure.

## Exercise Instructions:

You are provided with a JSON file representing a product assembly.
Your tasks are as follows:

1. **Add a new component**: Add a new component to the "components" array with the following details:
    - id: "COMP-56789"
    - name: "Component 3"
    - quantity: 7
    - unitOfMeasure: "UNIT"
    - description: "This component is used in the Product A Assembly for testing purposes."
    - supplier: "Supplier C"
    - leadTime: 2
    - cost: 20.0

2. **Update a sub-assembly property**: The product assembly's name has been updated to include the word "V2". Update the "name" field of the "assembly" object to reflect this change.

3. **Remove an unused component**: Remove the "Component 1" with id "COMP-12345" from the "components" array, as it is no longer needed in the product assembly.

4. **Restructure the components data**: Move the "supplier", "leadTime", and "cost" fields into a nested object called "component_details" within each component's JSON object.

5. **Add an additional field to the assembly object**: Add a new field called " manufacturing_date" with a placeholder value of "2022-01-01" to the "assembly" object, representing when the product was first manufactured.