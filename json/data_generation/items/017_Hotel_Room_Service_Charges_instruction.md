Here's an exercise instruction based on the given JSON object:

# Modify and Extend a Room Service Charge JSON Object

## Objective:
The goal of this exercise is to modify and extend a room service charge JSON object by adding new properties, updating existing values, and reorganizing the structure.

## Exercise Instructions:

You are provided with a JSON file representing a room service charge. Your tasks are as follows:

1. **Add historical charges**: Add a new entry to the `roomServiceChargeHistory` section with the following details:
	* `id`: a unique identifier (e.g., "38400004-8cf0-11bd-b23e-10b96e4ef00d")
	* `roomNumber`: "303"
	* `guestName`: "John Doe"
	* `date`: "2023-03-09"
	* `time`: "14:30"
	* `items`:
		+ A new item with the name "Chicken Soup", description, quantity, and unit price
2. **Update total charges**: Update the `totalCharges` field in the `roomServiceChargeHistory` section to reflect the new charge.
3. **Modify existing charge**: Find the entry for March 7th and update the charge for the item "Club Sandwich" by reducing its quantity from 1 to 0 (remove the item).
4. **Reorganize the charges history**: Sort the entries in the `roomServiceChargeHistory` section in descending order based on the date.
5. **Add a new field**: Add a new field called `numberOfGuests` to each entry in the `roomServiceChargeHistory` section with a value of 2 (assuming all room service charges are for two guests).