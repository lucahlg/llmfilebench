Here is an exercise instruction based on the given JSON object:

# Modify and Extend a Company JSON Object

## Objective:
The goal of this exercise is to modify and extend a company profile JSON object by adding new properties, updating existing values, reorganizing the structure, and removing unnecessary information.

## Exercise Instructions:

You are provided with a JSON file representing a company.
Your tasks are as follows:

1. **Update contact info**: Update John Smith's phone number to (987) 654-3210.
2. **Add new procedure**: Add a new procedure called "Weather Emergency" to the procedures array. The new procedure should have the following details:
	* name: "Severe Weather Warning"
	* description: "In the event of severe weather, all employees should take necessary precautions and follow emergency guidelines."
	* steps: ["Monitor local news for updates", "Take necessary precautions based on weather conditions", "Follow emergency guidelines from authorities"]
3. **Restructure location**: Move the location details into a nested object called "headquarters" with the structure:
```json
"headquarters": {
  "address": "123 Main Street",
  "city": "Anytown",
  "state": "CA",
  "zip": "12345"
}
```
4. **Remove redundant information**: Remove the "phone" field from John Smith's contact info and Jane Doe's contact info.
5. **Add new personnel member**: Add a new personnel member called "Bob Johnson" to the personnel array. The new member should have the following details:
	* name: "Bob Johnson"
	* role: "HR Representative"
	* contactInfo: {
		"phone": "(901) 234-5678",
		"email": "bob.johnson@acme.com"
	}