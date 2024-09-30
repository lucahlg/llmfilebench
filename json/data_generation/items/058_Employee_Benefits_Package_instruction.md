##  Analyze and Modify Employee Benefit Data

**Objective:** This exercise aims to familiarize you with manipulating JSON data structures by analyzing and modifying employee benefit information.

**Exercise Instructions:**

You are provided with a JSON file detailing a list of employee benefits and the overall package cost. Your tasks are as follows:

1. **Cost Analysis:** Calculate the total cost of all individual benefits listed in the "benefits" array and compare it to the "cost" field for the entire package.  Determine if there is a discrepancy and explain the possible reasons for any difference. 
2. **Benefit Modification:** Add a new benefit to the "benefits" array with the following details:

    - `"name"`: "Paid Time Off"
    - `"description"`: "Provides employees with paid time off for vacation, sick leave, and personal days."
    - `"cost"`: 75
    - `"coverage"`: "Accrual based on tenure"

3. **Coverage Update:**  Modify the description of the "Retirement Savings Plan" benefit to include information about employer matching contributions. For example, you could add: "Employer match up to 3% of employee contribution."
4. **Data Extraction:** Create a new JSON object that only includes the names and costs of all benefits in the package.

```json
{
  "benefit_names_and_costs": [
    {"name": "Health Insurance", "cost": 100},
    {"name": "Dental Insurance", "cost": 50},
    // ... (Include the remaining benefits)
  ]
}
```

**Remember:** Save your modified JSON file and ensure it is properly formatted.