import json
import random
import string
import os

# Path to your JSON file
json_path = "D:/Python/BTD6/AutoBTD6Storage/files.json"  # Update if needed

def generate_random_id(existing_ids):
    """Generate a unique 6-character uppercase alphanumeric ID."""
    while True:
        random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
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

# Get directory path from the user
directory_path = input("Enter the directory path to scan: ").strip()

# Validate directory path
if not os.path.isdir(directory_path):
    print("Invalid directory path. Please enter a valid path.")
    exit()

existing_paths = set(json_data.values())  # Track existing file paths to avoid duplicates

# Walk through the directory and add missing files
for root, _, files in os.walk(directory_path):
    for file in files:
        full_path = os.path.join(root, file)

        # Find the position of '/Maps/' in the path
        try:
            maps_index = full_path.lower().index("maps\\")  # Ensure it's case-insensitive
            relative_path = full_path[maps_index:].replace("\\", "/")  # Convert to forward slashes
        except ValueError:
            continue  # Skip files not inside 'Maps/'

        if relative_path not in existing_paths:
            unique_id = generate_random_id(json_data.keys())
            json_data[unique_id] = relative_path
            print(f"Added: {relative_path} with ID: {unique_id}")

# Save updated JSON
with open(json_path, "w", encoding="utf-8") as file:
    json.dump(json_data, file, indent=2)

print("JSON updated successfully.")