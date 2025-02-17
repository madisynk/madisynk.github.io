// Use in Mongosh to add a validator to the animal shelter database
db.createCollection("animals", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            title: "Animal Object Validation",
            // Requires all fields to be filled out
            required: ["animal_type", "breed", "sex_upon_outcome", "age_upon_outcome_in_weeks"],
            properties: {
                // Only allows for a string data type
                animal_type: {
                    bsonType: "string",
                    description: "Animal type must be a string and is required"
                },
                // Only allows for a string data type
                breed: {
                    bsonType: "string",
                    description: "Breed must be a string and is required"
                },
                // Only allows for a string data type
                sex_upon_outcome: {
                    bsonType: "string",
                    description: "Sex upon outcome must be a string and is required"
                },
                // Only allows for a int data type between 1 and 700
                age_upon_outcome_in_weeks: {
                    bsonType: "int",
                    minimum: 1,
                    maximum: 700,
                    description: "Age upon outcome in weeks must be an integer and between 1 and 700 and is required"
                }
            }
        }
    }
})