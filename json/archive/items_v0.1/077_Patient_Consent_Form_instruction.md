Here's an exercise instruction based on the provided JSON object:

# Modify a Medical Record JSON Object

## Objective:
The goal of this exercise is to modify and extend a medical record JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the data.

## Exercise Instructions:

You are provided with a JSON file representing a patient's medical record.
Your tasks are as follows:

1. Update the procedure: Change the "procedure" property from "Appendectomy" to "Hysterectomy".
2. Add a new property to the patient object: Add a new field called "dateOfBirth" to the patient object, with value "1990-05-12".
3. Modify an existing property in the hospital object: Update the phone number of the Springfield General Hospital from "555-345-6789" to "555-901-2345".
4. Remove the witness information: Delete the entire "witness" object from the JSON, including its properties.
5. Restructure the data: Move the "date" field into a nested object called "appointmentInfo" with the following structure:
```json
"appointmentInfo": {
    "scheduledDate": "2023-03-08",
    "signatureDate": "Signature Date"
}
```
Note that you should update the signatureDate property to reflect the actual date of signing, if different from the scheduled date.
6. Add a new field to the additionalInfo object: Append a statement indicating that the patient has been given the opportunity to review and sign the consent form.
7. Change the signature: Update the "signature" property to include the title "Patient Signature:" followed by the patient's name ("Emma Watson").