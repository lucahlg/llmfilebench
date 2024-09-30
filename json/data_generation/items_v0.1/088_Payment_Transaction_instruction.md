# Payment Transaction JSON Modification and Extension
## Objective:
The goal of this exercise is to modify and extend a payment transaction JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a payment transaction.
Your tasks are as follows:

1. **Payment Method Update**: The customer wants to change their payment method from credit card to PayPal. Update the "payment_method" object to reflect this change, including adding the necessary fields for PayPal (e.g., "paypal_id", "paypal_email").
2. **Merchant Information Addition**: Add a new property called "merchant_info" to the JSON, which should contain additional details about the merchant:
    - "website": "https://acme.com"
    - "phone_number": "+1-555-1234"
3. **Status Change and Timestamp Update**: The transaction status is updated to "declined". Also, update the timestamps ("created_at" and "updated_at") to reflect the new date of March 9th.
4. **Customer Information Restructure**: Move the customer's name into a nested object called "customer_info" with the structure:
```json
"customer_info": {
    "first_name": "John",
    "last_name": "Smith"
}
```
5. **ID Generation for Merchant and Customer**: In addition to updating the existing IDs, generate new IDs for both the merchant and customer using a library of your choice.

## Note:
You should ensure that all required changes are made within the given JSON structure, without introducing any unnecessary fields or modifications.