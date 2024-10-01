Here's a new exercise instruction based on the given JSON object:

**Modify and Extend a Project Plan**

## Objective:
The goal of this exercise is to modify and extend a project plan JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a project plan.
Your tasks are as follows:

1. **Add a new action**: Add a new action to the "planActions" array with the following details:
    - id: "ACTION-3"
    - action: "Conduct stakeholder analysis"
    - actionDueDate: "2023-03-29"
    - actionStatus: "Not Started"
    - actionResponsible: "Bob Johnson"
    - actionNotes: "Identify key stakeholders, assess their interests and influence."
2. **Update an existing document**: Update the revision of the "Project Plan" document to 1.5.
3. **Remove a document**: Remove the "System Architecture Design" document from the "planDocuments" array.
4. **Restructure the data**: Move the "supplier" field into a nested object called "project_info" with the structure:
```json
"project_info": {
    "supplier_name": "Acme Corporation",
    "supplier_contact": "john.smith@example.com"
}
```
5. **Change the plan status**: Update the "planStatus" to "On Hold".

Note: You should also make sure that any changes you make to the JSON structure are reflected in the corresponding variable names and data types in your code.