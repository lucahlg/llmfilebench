Here's an exercise instruction for your students:

# Modify and Extend a Research Proposal JSON Object

## Objective:
The goal of this exercise is to modify and extend a research proposal JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing a research proposal.
Your tasks are as follows:

1. **Add a new team member**: Add a new member to the "researchTeamMembers" array with the following details:
	* name: "Dr. Sophia Patel"
	* role: "Research Coordinator"
2. **Update budget categories**: Increase the "equipment" category by 25% and decrease the "travel" category by 15%. Make sure the total budget amount remains unchanged.
3. **Modify research proposal structure**: Move the "backgroundAndSignificance", "methods", and "expectedOutcomes" fields into a nested object called "researchProposalDetails". The resulting JSON should be structured as follows:
```
"researchProposal": {
    ...
    "researchProposalDetails": {
        "backgroundAndSignificance": "...",
        "methods": "...",
        "expectedOutcomes": "..."
    }
}
```
4. **Remove redundant information**: Remove the "specificAims" field from the JSON object, as it is deemed redundant with the rest of the proposal details.
5. **Change submission date and status**: Update the "dateSubmitted" to "2023-05-15" and change the "status" to "Under Review".