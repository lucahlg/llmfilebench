Here's an exercise instruction based on the given JSON object:

**# Modify and Extend a Corporate Agreement JSON Object**

## **Objective:**
The goal of this exercise is to modify and extend a corporate agreement JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## **Exercise Instructions:**

You are provided with a JSON file representing a corporate agreement.
Your tasks are as follows:

1. **Add a new shareholder:** Add a new shareholder named "Charlie Brown" to the "shareholders" array. The "person" object should contain:
	* "name": "Charlie Brown"
	* "address": {
		+ "streetAddress": "789 Oak Street",
		+ "city": "Anytown",
		+ "state": "CA",
		+ "zip": "12345"
	}
2. **Update voting procedures:** Update the "votingProcedures" property to reflect a new procedure where shareholders vote by a two-thirds majority of the shares outstanding.
3. **Remove capital contributions:** Remove the "capitalContributions" property from the JSON object, as it is no longer relevant.
4. **Restructure signatures:** Move the "signatures" array into a nested object called "corporateAgreementDetails" with the structure:
```json
"corporateAgreementDetails": {
    "signatures": [...],
    "effectiveDate": [...]
}
```
Note: Leave the existing properties and values in place, only restructure the JSON as specified.

## **Deliverables:**

Your modified and extended corporate agreement JSON object should be submitted in a single file. Please ensure that all required fields are included, and no unnecessary data is added or removed.