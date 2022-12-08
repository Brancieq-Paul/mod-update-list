#!/usr/bin/env python3
import json
from src.const import Paths
import pathlib

# Output tool name: mod-update-list
print("MOD-UPDATE-LIST SETUP")

# Open default config file
with open(Paths.INTERNAL_DEFAULT_CONFIG, 'r') as f:
    config = json.load(f)

    # Input curseforge pack path
    config["cf_pack_path"] = input("Curseforge pack path: ").replace("\\", "/").replace("\"", "")
    # Add trailing slash if not present
    if not config["cf_pack_path"].endswith("/"):
        config["cf_pack_path"] += "/"

    # Input curseforge api key
    config["cf_api_key"] = input("Curseforge api key: ")

# Save config file
with open(Paths.INTERNAL_CONFIG, 'w') as f:
    json.dump(config, f)

# Open .env file
with open(".env", 'w') as f:
    # Get current working directory absolute path
    current_working_directory = pathlib.Path(__file__).parent.resolve()

    # Write PYTHONPATH
    f.write(f"PYTHONPATH={current_working_directory}")
    

# Output end of setup
print("Setup completed.")
