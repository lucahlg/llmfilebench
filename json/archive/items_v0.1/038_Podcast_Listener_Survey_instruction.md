Here's an exercise instruction based on the given JSON object:

# Analyze and Refine Listener Data

## Objective:
The goal of this exercise is to analyze and refine listener data by modifying, restructuring, and extracting specific information from a given JSON object.

## Exercise Instructions:

You are provided with a JSON file containing listener data. Your tasks are as follows:

1. Extract personal info: Create a new property called "personal_details" within the "listener" object. This should contain the following fields:
	* "age": 35 (as is, no change needed)
	* "gender": "female"
	* "education": "college degree"
2. Update podcast preferences: Add a new field to the "podcast_preferences" object called "favorite_genres". It should contain an array with the top two preferred genres, which are "news" and "comedy".
3. Calculate average time spent listening: Update the "listening_habits" object by adding a new property called "total_listening_time". This should be calculated by multiplying the "average_time" (30) by the frequency of daily podcast listening.
4. Remove additional comments: Remove the "additional_comments" field from the JSON object, as it's no longer relevant to the analysis.
5. Restructure data for visualization: Move the "podcast_preferences" and "listening_habits" objects into a new nested object called "listener_behavior", with the structure:
```json
"listener_behavior": {
  "podcast_preferences": {
    // existing fields here...
  },
  "listening_habits": {
    // existing fields here...
  }
}
```

Your task is to write code that accomplishes these modifications and restructuring, while maintaining the integrity of the original data.