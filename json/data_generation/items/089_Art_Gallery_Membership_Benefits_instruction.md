Here is an exercise instruction for the given JSON object:

# Modify and Extend Membership Rewards JSON
## Objective:
The goal of this exercise is to modify and extend the membership rewards JSON object by adding, updating, and removing properties. You will also be asked to restructure part of the JSON.

## Exercise Instructions:

You are provided with a JSON file representing membership rewards for an art gallery.
Your tasks are as follows:

1. Add a new membership type: Add a new membership type called "Student Membership" with the following details:
    - name: Student Membership
    - cost: 25 (discounted rate for students)
    - duration: 1 year
    - benefits:
        + Free admission to the art gallery for up to 2 students
        + 5% discount on art purchases
2. Update an existing membership type: Increase the cost of the "Family Membership" by $10.
3. Add a new benefit to an existing membership type: Add a new benefit called "Complimentary exhibition catalog" to the "Patron Membership".
4. Restructure the data: Move the "benefits" field into a nested object called "membership_details" with the structure:
    json	
    "membership_details": {
        "individual_membership": [
            {
                "name": "Free admission to the art gallery",
                "description": "Members receive free admission to the art gallery, including special exhibitions."
            },
            {
                "name": "10% discount on art purchases",
                "description": "Members receive a 10% discount on all art purchases, including prints, paintings, and sculptures."
            }
        ],
        "family_membership": [
            {
                "name": "Free admission to the art gallery for up to 2 adults and 2 children",
                "description": "Family members receive free admission to the art gallery, including special exhibitions."
            },
            {
                "name": "15% discount on art purchases",
                "description": "Family members receive a 15% discount on all art purchases, including prints, paintings, and sculptures."
            }
        ],
        "patron_membership": [
            {
                "name": "Free admission to the art gallery for up to 4 adults and 4 children",
                "description": "Patron members receive free admission to the art gallery, including special exhibitions."
            },
            {
                "name": "20% discount on art purchases",
                "description": "Patron members receive a 20% discount on all art purchases, including prints, paintings, and sculptures."
            }
        ]
    }