Here's an exercise instruction based on the given JSON object:

# Financial Report Modification Exercise

## Objective:
The goal of this exercise is to modify a financial report JSON object by adding new data, updating existing values, and reorganizing the structure.

## Exercise Instructions:

You are provided with a JSON file representing a company's financial report. Your tasks are as follows:

1. **Add New Expense Category**: Add a new expense category called "Travel and Training" to the expenses array. The amount for this category should be $8000.
2. **Update Revenue**: Increase the revenue by 10% from its current value.
3. **Remove Notes Field**: Remove the notes field from the JSON object, as it's no longer relevant.
4. **Restructure Expenses**: Move each expense category to a separate JSON object within the expenses array, with the following structure:
```json
"expenses": [
    {
        "category": "Salaries and Wages",
        "amount": 50000,
        "details": "Breakdown of salaries and wages for employees"
    },
    {
        "category": "Rent and Utilities",
        "amount": 10000,
        "details": "Details on rent, utilities, and other related expenses"
    },
    {
        "category": "Marketing and Advertising",
        "amount": 5000,
        "details": "Information on marketing campaigns and advertising expenses"
    },
    {
        "category": "Travel and Training",
        "amount": 8000,
        "details": "Details on travel-related expenses for employees"
    }
]
```
5. **Calculate New Profit**: Recalculate the profit based on the updated revenue and total expenses (including the new category).