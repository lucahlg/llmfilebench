Here's an exercise instruction based on the given JSON object:

# Modify and Extend a Key Management System (KMS) JSON Object

## Objective:
The goal of this exercise is to modify and extend a KMS JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a cryptographic key.
Your tasks are as follows:

1. **Add rotation details**: Add a new property called "rotationDetails" to the JSON. The "rotationDetails" should contain the following fields:
    - "rotationWindow": "14d"
    - "nextRotationTimeWarning": "7d"

2. **Update protection level**: Update the "protectionLevel" property from "HSM" to "SOFTWARE".
3. **Remove algorithm information**: Remove the "algorithm" field from both the top-level JSON and the "keyVersion" array.
4. **Reorganize labels**: Move the "labels" object into a nested object called "metadata" with the structure:
    json
    {
        "team": "alpha"
        ...
    }

5. **Update key version information**: Update the "name" field in the first "keyVersion" object to include the project ID and location, e.g., "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/456".

Note: Your code should handle any potential errors that might occur during modification or rotation.