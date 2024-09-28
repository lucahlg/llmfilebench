Here's an exercise instruction based on the given JSON object:

# Modify and Enhance a Product and Recommendation JSON Object

## Objective:
The goal of this exercise is to modify and enhance a product and recommendation JSON object by adding, updating, removing properties, and restructuring part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a product and its recommendations. Your tasks are as follows:

1. **Add a new property**: Add a new field called "rating" to the "product" object. The rating should be an average based on customer reviews, calculated from the existing price.
2. **Update an existing recommendation**: Update the timestamp of one of the recommendations to reflect the current date and time (i.e., `2023-03-09T14:30:00Z`).
3. **Remove a tag**: Remove the "gadgets" tag from the product's tags array.
4. **Restructure data**: Move the "category" field into a nested object called "product_info" with the structure:
    ```json
    "product_info": {
        "category": "Electronics",
        "subcategory": "Smartphones"
    }
    ```
5. **Add a new recommendation**: Add a new recommendation for the product with the following details:
    - `productId`: "prod_123"
    - `reason`: "You have purchased products from this brand before."
    - `score`: 0.9
    - `timestamp`: The current date and time (i.e., `2023-03-09T14:30:00Z`)

Your solution should modify the original JSON object to reflect these changes.