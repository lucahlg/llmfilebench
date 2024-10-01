Here's an exercise instruction based on the given JSON object:

# Modify and Restructure a Service Agreement JSON Object

## Objective:
The goal of this exercise is to modify and restructure a service agreement JSON object by adding new properties, updating existing values, and reorganizing the structure.

## Exercise Instructions:

You are provided with a JSON file representing a service agreement. Your tasks are as follows:

1. **Add a new service**: Add a new service type called "backupService" to the "services" array. The description of this service should be: "Automatic backups of your website files every night." and it should have a price of $2.0.
2. **Update agreement terms**: Update the "terminationTerms" field to include an additional condition for termination, which states that any outstanding balance must be paid in full before termination can occur.
3. **Move service details into a nested object**: Move the details of each service type (i.e., "description", "price") into a separate nested object within the "services" array. For example:
```json
{
    "serviceType": "webHosting",
    "details": {
        "description": "Shared web hosting with 10GB of storage and unlimited bandwidth.",
        "price": 10.0
    }
}
```
4. **Remove unnecessary fields**: Remove the "additionalTerms" field from the JSON object, as it is no longer relevant.
5. **Update dates**: Update the "startDate" to "2023-03-01" and the "endDate" to "2024-02-28".