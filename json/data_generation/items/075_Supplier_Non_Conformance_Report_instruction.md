Here's an exercise instruction based on the given JSON object:

# Modify and Restructure a Non-Conformance Report (NCR) JSON Object
## Objective:
The goal of this exercise is to modify and restructure a non-conformance report (NCR) JSON object by adding new properties, updating existing values, and reorganizing the structure.

## Exercise Instructions:

You are provided with a JSON file representing an NCR. Your tasks are as follows:

1. Update the impacted quantity: The supplier has corrected the material defect in 50 of the affected widgets. Update the "impactedQuantity" field to reflect this correction.
2. Add a new attachment: Add a new attachment called "Supplier Root Cause Analysis Report.pdf" with the following details:
    - attachmentName: "Supplier Root Cause Analysis Report.pdf"
    - attachmentType: "PDF"
    - attachmentUrl: "https://example.com/supplier-root-cause-analysis-report.pdf"
3. Update the report status: The NCR has been closed after the supplier implemented corrective actions. Update the "reportStatus" field to reflect this change.
4. Restructure the attachments array: Move all the attachments into a nested object called "documents" with the following structure:
```json
'documents': {
    'attachment1': {
        'attachmentName': 'Supplier Corrective Action Plan.pdf',
        'attachmentType': 'PDF',
        'attachmentUrl': 'https://example.com/supplier-corrective-action-plan.pdf'
    },
    'attachment2': {
        'attachmentName': 'Supplier Inspection Report.docx',
        'attachmentType': 'Word Document',
        'attachmentUrl': 'https://example.com/supplier-inspection-report.docx'
    },
    'newAttachment': {
        'attachmentName': 'Supplier Root Cause Analysis Report.pdf',
        'attachmentType': 'PDF',
        'attachmentUrl': 'https://example.com/supplier-root-cause-analysis-report.pdf'
    }
}
```
5. Remove the "rootCauseAnalysis" field: This information is now included in one of the attachments.

Note: Make sure to preserve the existing structure and formatting of the JSON object during your modifications.