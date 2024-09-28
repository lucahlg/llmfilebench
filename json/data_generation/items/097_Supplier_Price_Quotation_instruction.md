Here is an exercise instruction based on the given JSON object:

**# Modify and Extend a Quotation JSON Object**

## **Objective:**
The goal of this exercise is to modify and extend a quotation JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## **Exercise Instructions:**

You are provided with a JSON file representing a supplier quotation.
Your tasks are as follows:

1. **Add a new item**: Add a new item to the "items" array with the following details:
	* itemId: "ITEM-1003"
	* description: "Widget C"
	* unitPrice: 20.0
	* quantity: 7
2. **Update an existing property**: Update the "expirationDate" to reflect a new expiration period of June 15th, 2023.
3. **Modify the supplier information**: Update the "supplierName" to "Acme Suppliers Inc." and add a new field called "contactPerson" with the value "John Smith".
4. **Restructure the data**: Move the "totalCost" calculation into a nested object called "summary" with the structure:
json
"summary": {
	"subTotal": 150.0,
	"tax": 10.0,
	"total": 160.0
}
5. **Remove an existing property**: Remove the "quotationDate" field from the JSON object.

Note: You will need to perform calculations (e.g., subTotal, tax) based on the existing data and update the totalCost value accordingly in the new structure.