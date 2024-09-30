Based on the provided JSON object, here's an exercise instruction for your students:

# Modify and Extend a TV Show Database

## Objective:
The goal of this exercise is to modify and extend a database of popular TV shows by adding, updating, and removing properties. You will also be asked to restructure part of the data.

## Exercise Instructions:

You are provided with a JSON file representing a collection of TV shows.
Your tasks are as follows:

1. **Add a new property**: Add a new property called "productionCompany" to each TV show object. The "productionCompany" should contain the following fields:
    - "name": "Universal Studios"
2. **Update ratings**: Update the rating for "The Office" to 9.0 and increase its count by 20,000.
3. **Remove genres**: Remove the "Action" genre from "Game of Thrones".
4. **Restructure genres**: Move the "genres" array into a nested object called "showDetails" with the following structure:
    json
    "showDetails": {
        "genre1": "Comedy",
        "genre2": "Drama"
    }
5. (Optional) If you'd like to make it more challenging, you could also add a new property called "awards" to each TV show object and populate it with a list of notable awards won by the show.

This exercise should test your students' ability to manipulate JSON data, update values, remove properties, and restructure the structure of the data.