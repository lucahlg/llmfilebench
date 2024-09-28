# Modify and Extend a Prescription JSON Object

## Objective:
The goal of this exercise is to modify and extend a prescription JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a patient's prescription.
Your tasks are as follows:

1. **Add a new medical condition**: Add a new field called "medicalCondition" to the "patient" object, listing an additional health issue affecting the patient:
    - value: "Diabetes"
2. **Update medication details**: The prescribed medication has been recalled. Update the "medication" object with the following changes:
    - **Change dosage**: Increase the daily dosage of Albuterol to 300 mcg.
    - **Update instructions**: Change the inhalation instructions to "Inhale 3 puffs every 6-8 hours as needed for shortness of breath."
3. **Remove pharmacy details**: The patient has chosen a different pharmacy for future prescriptions. Remove the entire "pharmacy" object from the JSON.
4. **Restructure prescription data**: Move the date of expiration and status into a nested object called "prescriptionInfo" with the structure:
```json
{
    "expirationDate": "2023-09-07",
    "status": "active"
}
```
5. (Optional) If you have time, add an additional task to your exercise: Add a new property called "prescriber" to the JSON object. The prescriber should contain the following details:
    - **Name**: "Dr. Jane Smith"
    - **Title**: "MD, FACC"
    - **Phone Number**: "(555) 123-4567"

Note: You can choose to include or exclude this additional task based on your preference and the time you want to allocate for the exercise.