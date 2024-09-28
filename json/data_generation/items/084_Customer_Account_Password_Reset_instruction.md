Here's an exercise instruction for the given JSON object:

# Secure a Customer Profile by Modifying and Validating Credentials

## Objective:
The goal of this exercise is to modify and validate a customer profile JSON object by updating existing values, adding new properties, and ensuring secure password practices.

## Exercise Instructions:

You are provided with a JSON file representing a customer profile. Your tasks are as follows:

1. Validate passwords: Check if the "newPassword" and "confirmPassword" fields match each other. If they do not match, update both fields to be identical.
2. Add a new property: Include an additional security measure by adding a "password_expires" field with a default value of 30 days (e.g., in Unix timestamp format).
3. Update the email address: Change the customer's email address from "james.smith@example.com" to "james.smith2@example.com".
4. Restructure and encrypt passwords: Move the password fields into a nested object called "credentials" with the structure:
```json
"credentials": {
  "password": "$hashedPassword",
  "confirm_password": "$hashedConfirmPassword"
}
```
Replace the plain text passwords with hashed versions using a suitable hashing algorithm (e.g., bcrypt, scrypt). Ensure that both password fields are properly encrypted.

5. Optional Challenge: Enhance security by adding an additional validation step for the customer's email address before updating it. You can achieve this by sending a verification email to the updated email address and only updating the original JSON if the verification link is clicked within a certain timeframe (e.g., 1 hour).

This exercise requires students to manipulate and validate a customer profile JSON object, ensuring secure password practices while also introducing new properties and restructuring the existing data.