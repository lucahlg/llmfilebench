Here's an exercise instruction for the given JSON object:

**# Modify and Extend an Invoice JSON Object**

## **Objective:**
The goal of this exercise is to modify and extend an invoice JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## **Exercise Instructions:**

You are provided with a JSON file representing an invoice.
Your tasks are as follows:

1. **Update Invoice Date**: Update the "invoice_date" property to reflect the current date (2023-03-20).
2. **Add New Customer Information**: Add a new property called "customer_representative" to the customer object, containing the following fields:
	* name: "John Smith"
	* phone_number: "555-1234"
	* email: "john.smith@example.com"
3. **Remove Unnecessary Fields**: Remove the "description" field from each item in the "items" array.
4. **Restructure Item Data**: Move the "quantity", "unit_price", and "total_price" fields into a nested object called "pricing_info" for each item, preserving their values.
5. **Add Total Invoice Amount**: Calculate and add a new property called "total_amount" to the invoice object, which represents the sum of the total prices of all items.

Note: The tasks are designed to challenge your understanding of JSON manipulation and restructuring, while also introducing you to real-world scenarios involving invoices and customer data.