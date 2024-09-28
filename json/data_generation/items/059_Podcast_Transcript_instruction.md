# Modify a Podcast JSON Object
## Objective:
The goal of this exercise is to modify and restructure a podcast JSON object by adding new segments, updating existing values, and reorganizing the structure.

## Exercise Instructions:

You are provided with a JSON file representing a podcast episode.
Your tasks are as follows:

1. Add a new segment to the "segments" array with the following details:
    - start time: "00:30:00"
    - end time: "00:40:00"
    - speakers: ["Jane Doe", "John Smith"]
    - content: Discuss the future of the Internet and its potential impact on society.
2. Update the "publicationDate" to reflect a new release date: "2023-06-15".
3. Remove the "authors" array from the JSON object, as it is not relevant to this episode.
4. Add a new property called "genre" to the podcast object with the value "Technology".
5. Restructure the "segments" array by moving the third segment's content into a nested object called "summary". The summary should contain a brief description of the third segment's content.

Note: Be sure to update any relevant field values and formats (e.g., timestamps) as part of your modifications, following standard JSON formatting practices.