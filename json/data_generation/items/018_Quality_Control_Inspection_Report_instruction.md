Here's an exercise instruction based on the given JSON object:

# Modify and Extend a Quality Inspection Report JSON Object

## Objective:
The goal of this exercise is to modify and extend a quality inspection report JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a quality inspection report.
Your tasks are as follows:

1. Add a new inspection item to the "inspectionItems" array:
	* id: "ITEM-004"
	* name: "Labeling and Branding Compliance"
	* description: "Inspection of the product's labeling and branding for compliance with company standards."
	* inspectionCriteria: [
		"Check for correct logo placement",
		"Verify brand name and tagline accuracy"
	]
	* inspectionResults: [
		"No issues found",
		"All branding elements match company guidelines"
	]
	* status: "passed"

2. Update the overallStatus of the report to "partially passed". Also, update the comments field with a new message:
	* The report now indicates that one inspection item has failed.

3. Remove the "description" property from all inspection items in the "inspectionItems" array.

4. Add a new nested object called "regulatoryCompliance" to the root of the JSON. This object should contain information about the product's regulatory compliance, including:
	* industry: "Food and Beverage"
	* certificationDate: "2023-02-15"
	* certificationNumber: "123456"

5. Restructure the inspectionResults arrays for each item by adding a new nested array called "details". This array should contain more detailed information about each result, including:
	* description of the finding
	* corrective action taken

Note that this exercise requires you to add, update, and remove properties, as well as restructure part of the JSON object.