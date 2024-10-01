Here's a new exercise instruction based on the given JSON object:

# Modify and Extend a Reservation JSON Object

## Objective:
The goal of this exercise is to modify and extend a reservation JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a customer's travel reservation.
Your tasks are as follows:

1. **Add special request**: Add a new special request to the `specialRequests` array with the following details:
	* Request: "Early check-in"
2. **Update travel activity price**: Update the `activityPrice` of the Grand Canyon Helicopter Tour to $249.99.
3. **Remove customer email field**: Remove the `customerEmail` property from the `customer` object.
4. **Restructure location information**: Move the `locationAddress` field into a nested object called `locationInfo` within the `activityLocation` object, with the structure:
```json
"locationInfo": {
    "addressLine1": "Grand Canyon Village",
    "city": "Tusayan",
    "state": "AZ",
    "postalCode": "86023",
    "country": "USA"
}
```
5. **Add provider contact information**: Add a new `providerContact` property to the `activityProvider` object with the following details:
	* Phone number: 555-901-2345
	* Email address: providersupport@maverickhelicopters.com

## Bonus Task (Optional):
Consider adding a new section to the JSON file called `reservationSummary`, which should contain a brief summary of the reservation, including the activity name, date, and total price. Make sure to keep this task optional so students can choose whether or not to attempt it.