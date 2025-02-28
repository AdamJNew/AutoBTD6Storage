import json
import random
import string
import os

# Path to your JSON file
json_path = "D:/Python/BTD6/AutoBTD6Storage/files.json"  # Update this if needed

# Function to generate a unique 6-character uppercase alphanumeric ID
def generate_random_id(existing_ids):
    while True:
        random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))  # Only uppercase + digits
        if random_id not in existing_ids:
            return random_id

# Load existing JSON or create a new one
if os.path.exists(json_path):
    with open(json_path, "r", encoding="utf-8") as file:
        try:
            json_data = json.load(file)
        except json.JSONDecodeError:
            json_data = {}
else:
    json_data = {}

# Get new file path from the user
new_file_path = input("Enter the new file path: ")

# Generate a unique uppercase ID
unique_id = generate_random_id(json_data.keys())

# Add the new file path under the generated uppercase ID
json_data[unique_id] = new_file_path

# Save updated JSON
with open(json_path, "w", encoding="utf-8") as file:
    json.dump(json_data, file, indent=2)

print(f"File path added successfully with ID: {unique_id}")
