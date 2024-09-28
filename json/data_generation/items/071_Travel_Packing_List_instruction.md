Here's an exercise instruction based on the given JSON object:

**# Refine and Extend a Travel Itinerary**

## Objective:
The goal of this exercise is to refine and extend a travel itinerary JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a trip to Paris.
Your tasks are as follows:

1. **Add new items**: Add two new items to the "items" array. The first item should have:
	* name: "River Seine Cruise"
	* quantity: 1
	* notes: "Enjoy a romantic evening cruise along the Seine."
	* tags: ["relaxing", "scenic"]
The second item should have:
	* name: "Montmartre Art Museum"
	* quantity: 2
	* notes: "Visit the museum to see works by famous artists like Monet and Renoir."
	* tags: ["art", "culture"]
2. **Update existing categories**: Update the "categories" array to include a new category called "Nature". The "Nature" category should have:
	* name: "Nature"
	* description: "Parks, gardens, and other green spaces to explore."
3. **Modify a property**: Update the start date of the trip from 2023-03-08 to 2023-02-22.
4. **Restructure the data**: Move the "tags" array into a nested object called "metadata" for each item in the "items" array, with the structure:
```
{
    ...
    "items": [
        {
            ...
            "metadata": {
                "type": ["must-see", "iconic"]
            }
        },
        {
            ...
            "metadata": {
                "theme": ["art", "history"]
            }
        },
        ...
    ]
}
```
Note: Only modify the existing data structure, do not add any new properties that are not explicitly mentioned.