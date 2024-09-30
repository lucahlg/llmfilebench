Here's a new exercise instruction based on the given JSON object:

# Modify and Extend an SLA JSON Object

## Objective:
The goal of this exercise is to modify and extend a Service Level Agreement (SLA) JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a Gold SLA.
Your tasks are as follows:

1. **Add new service level objectives**: Add two new service level objectives to the "service_level_objectives" array. The new targets and metrics should be:
	* Name: "Error Rate"
	* Target: 0.01
	* Metric: "error_rate"
	* Name: "Response Time"
	* Target: 200
	* Metric: "response_time"
2. **Update the credits amount**: Increase the credits amount from 10% to 20%.
3. **Modify an existing metric**: Update the target of the "Latency" metric from 100ms to 90ms.
4. **Remove redundant data**: Remove the duplicate end date ("2024-12-31") from the "term" object, leaving only one entry for each start and end date.

Note: This exercise focuses on modifying existing properties, adding new ones, and reorganizing the JSON structure to improve its readability and maintainability.