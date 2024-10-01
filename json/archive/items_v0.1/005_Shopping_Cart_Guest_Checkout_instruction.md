Here's an exercise instruction based on the given JSON object:

**# Modify and Extend an E-commerce Order**

## **Objective:**
The goal of this exercise is to modify and extend a JSON object representing an e-commerce order. You will be asked to add, update, and remove properties, as well as restructure part of the JSON.

## **Exercise Instructions:**

You are provided with a JSON file representing an order.
Your tasks are as follows:

1. **Add a new shipping option**: Add a new property called "shippingMethod" to the JSON object. The "shippingMethod" should contain the following fields:
	* "method": "Express Shipping"
	* "cost": 9.99
2. **Update order details**: Update the quantity of the product with productId "P12345" to 3.
3. **Remove payment info**: Remove the entire "paymentInfo" object from the JSON, including its properties (cardNumber, expirationDate, cvv).
4. **Reorganize line items**: Move each product in the "lineItems" array into a separate "product" property, with the following structure:
```json
{
  "productId": "P12345",
  "quantity": 2,
  "unitPrice": 10.99,
  "imageUrl": "https://example.com/product-image.jpg"
}
```
5. **Add an order status**: Add a new property called "orderStatus" to the JSON object, with the value "Pending".

Note: You may need to use array manipulation and nested objects to complete this exercise!