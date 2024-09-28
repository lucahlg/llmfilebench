Here's an exercise instruction for the given JSON object:

**# Modify and Extend a Firewall Rule JSON Object**

## **Objective:**
The goal of this exercise is to modify and extend a firewall rule JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## **Exercise Instructions:**

You are provided with a JSON file representing a firewall rule for a web server.
Your tasks are as follows:

1. **Add a new property**: Add a new property called "description" to the JSON object at the root level. The description should read: "Allow HTTP traffic from port 80 and HTTPS traffic from port 443."
2. **Update an existing property**: Update the protocol property to reflect that it's also allowing UDP traffic.
3. **Remove a property**: Remove the `targetServiceAccounts` array from the JSON object, as it's not needed for this firewall rule.
4. **Restructure the data**: Move the `portRange` object into a nested object called `tcpPortRanges` with the structure:
```
{
  "tcp": {
    "startPort": 80,
    "endPort": 8080
  },
  "udp": {
    // add UDP port range here (example: startPort: 50000, endPort: 59999)
  }
}
```
Note: You should fill in the `udp` port range with a valid example.
5. **Modify an existing property**: Update the virtual machine name to "web-server-2" and its project ID to "my-new-project".

## **Example Output**:
The modified JSON object should look like this:
```json
{
  "name": "MyRule",
  "description": "Allow HTTP traffic from port 80 and HTTPS traffic from port 443.",
  "protocol": ["TCP", "UDP"],
  "tcpPortRanges": {
    "startPort": 80,
    "endPort": 8080
  },
  "udpPortRanges": {
    "startPort": 50000,
    "endPort": 59999
  },
  "virtualMachine": {
    "name": "web-server-2",
    "id": "1234567890123456789",
    "projectId": "my-new-project"
  },
  "firewall": {
    // ... (no changes to firewall object)
  }
}
```