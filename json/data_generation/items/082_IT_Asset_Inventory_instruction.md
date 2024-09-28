Here's an exercise instruction for the given JSON object:

# Modify and Restructure a Device JSON Object

## Objective:
The goal of this exercise is to modify and restructure a device profile JSON object by adding new properties, updating existing values, and reorganizing the structure.

## Exercise Instructions:

You are provided with a JSON file representing a laptop. Your tasks are as follows:

1. Add a new property called "condition" to the JSON object. The "condition" field should contain one of three possible values:
	* "new"
	* "used"
	* "refurbished"

2. Update the "purchaseDate" and "warrantyExpirationDate" fields by moving them into a nested object called "ownership_info". This new object should also include the "serialNumber" field.

3. Remove the "notes" field from the JSON object, as it is no longer relevant.

4. Change the "status" property to "inactive", since this laptop has been reassigned.

5. Add a new nested object called "technical_info" under the "device" root. This new object should contain the following fields:
	* "processor_type": "Intel Core i7"
	* "ram_capacity": "16 GB"

6. Update the "cost" field to reflect the current market value of this laptop.

**Note:** As a system administrator, you need to make sure that all changes are properly documented and saved to the original JSON file.