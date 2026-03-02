import json
import yaml
import os
from slugify import slugify

# Load the JSON file
with open("data/approved.json", "r") as f:
    drills = json.load(f)

# Ensure folders exist
os.makedirs("warmups", exist_ok=True)
os.makedirs("activities", exist_ok=True)
os.makedirs("games", exist_ok=True)

# Convert each drill to YAML
for drill in drills:
    drill_type = drill.get("type", "").lower()

    if drill_type == "warmup":
        folder = "warmups"
    elif drill_type == "activity":
        folder = "activities"
    else:
        folder = "games"

    slug = slugify(drill.get("name", "unnamed-drill"))
    path = f"{folder}/{slug}.yaml"

    with open(path, "w") as out:
        yaml.dump(drill, out, sort_keys=False)
