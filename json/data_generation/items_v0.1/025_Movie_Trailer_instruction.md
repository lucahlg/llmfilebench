Here's an exercise instruction based on the given JSON object:

# Modify and Extend a Movie JSON Object

## Objective:
The goal of this exercise is to modify and extend a movie profile JSON object by adding new properties, updating existing values, and reorganizing the structure.

## Exercise Instructions:

You are provided with a JSON file representing a movie. Your tasks are as follows:

1. **Add new cast members**: Add two new actors to the "castMembers" array. The new actors should be:
    - "Orlando Bloom" playing the role of "Legolas"
    - "John Rhys-Davies" playing the role of "Gimli"
2. **Update movie details**: Update the "releaseDate" property to reflect a re-release in 2003.
3. **Add new genre**: Add a new genre called "Drama" to the existing list of genres.
4. **Restructure the data**: Move the "castMembers" array into a nested object called "productionDetails" with the structure:
```
{
    "name": "The Lord of the Rings: The Fellowship of the Ring",
    "description": "...",
    "productionDetails": {
        "director": "...", // assume this is already in the original JSON
        "castMembers": [
            {...},
            {...}  // the new cast members added in step 1
        ]
    },
    ...
}
```
5. **Remove unnecessary properties**: Remove the "trailerFormat" and "trailerQuality" properties from the movie object, as they are no longer relevant.

## Bonus Task:**
Consider adding a nested object called "awards" to the movie object, containing details of notable awards won by the movie (e.g., Oscars, BAFTAs). However, this is an optional task and not required for completing the exercise.