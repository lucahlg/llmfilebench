Here's an exercise instruction based on the given JSON object:

# Modify and Extend a Hotel Reservation JSON Object

## Objective:
The goal of this exercise is to modify and extend a hotel reservation JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a hotel reservation.
Your tasks are as follows:

1. Add a new property called "guestInfo" to the "reservation" object. The "guestInfo" should contain the following fields:
    - "firstName": "Jane",
    - "lastName": "Doe",
    - "phoneNumber": "555-1234"
2. Update the "price" of the "roomType" to reflect a 10% discount, which is $22.50.
3. Modify the "startDate" and "endDate" of the reservation to start on August 15th and end on August 20th, respectively.
4. Change the status of the reservation from "booked" to "paid".
5. Restructure the data: Move the "name", "city", "state" fields into a nested object called "hotelInfo" with the structure:
```
{
    "hotelInfo": {
        "hotelId": string,
        "name": string,
        "city": string,
        "state": string
    }
}
```

Note: Make sure to maintain the original nesting structure of the JSON object and only modify the specified fields.