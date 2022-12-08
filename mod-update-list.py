#!/usr/bin/env python3
from src.CurseForgeVerif import verify_mod
from src.InstanceFile import InstanceFile
import sys

# Get args
args = sys.argv

# Get only the true args
args = args[1:]

# Should have at least one arg
if len(args) == 0:
    print("No version given")
    exit(1)

# Initialize list of mods to update
InstanceFile.load_instance_files()

# Verify if the mod exists for the given version
for instance_file in InstanceFile.instance_files:
    verify_mod(instance_file.project_id, args)
