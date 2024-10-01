Here's an exercise instruction based on the given JSON object:

# Modify and Enhance a Catalog JSON Object

## Objective:
The goal of this exercise is to modify and enhance a catalog JSON object by adding new properties, updating existing values, and reorganizing the structure.

## Exercise Instructions:

You are provided with a JSON file representing a catalog. Your tasks are as follows:

1. **Add a new TV show**: Add a new TV show called "Game of Thrones" to the "tvShows" array. The details for this TV show should include:
    - id: "50000000-0000-0000-0000-000000000001"
    - name: "Game of Thrones"
    - description: A brief summary of the show's plot.
    - posterUrl: The URL of a suitable image representing the show.

2. **Update an existing merchandise item**: Update the "price" of the "Friends Central Perk Mug" to 17.99 and change its availability status to false (i.e., it is no longer in stock).

3. **Add a new property to the catalog**: Add a new property called "featuredTvShow" to the top-level catalog object. This feature should highlight one TV show from the collection with an additional description, making it more prominent.

4. **Restructure the merchandise array**: Move all merchandise items into a nested object under each respective TV show's entry, keeping the same properties and values.
5. **Bonus Challenge**: Add a filter to only display catalogs where at least one merchandise item is in stock.