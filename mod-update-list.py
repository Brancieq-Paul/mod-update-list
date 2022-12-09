#!/usr/bin/env python3
from src.CurseForgeVerif import verify_mod
from src.InstanceFile import InstanceFile
import sys
import os

# Def pause for all systems
def pause():
    plat = sys.platform
    print(f"Platform: {plat}")
    if plat == "win32" or plat == "cygwin" or plat == "msys" or plat == "win64":
        os.system("pause")
    elif plat == "linux":
        os.system("read -p 'Press Enter to continue...' var")
    elif plat == "darwin":
        os.system("read -p 'Press Enter to continue...' var")

# Get args
args = sys.argv

# Get only the true args
args = args[1:]

# Get pause option in args
step_pause = False
if "--pause" in args or "-p" in args:
    step_pause = True
    if "--pause" in args:
        args.remove("--pause")
    if "-p" in args:
        args.remove("-p")

# Should have at least one arg
if len(args) == 0:
    print("No version given")
    exit(1)

# Initialize list of mods to update
InstanceFile.load_instance_files()

# Available mods count
available_mods = 0
not_available_mods = 0
# Verify if the mod exists for the given version
print(f"Verifying mods for versions {args}")
for instance_file in InstanceFile.instance_files:
    res = verify_mod(instance_file.project_id, args)
    if res:
        available_mods += 1
    else:
        not_available_mods += 1
    if step_pause:
        pause()

# Bilan
print(f"Available mods: {available_mods}")
print(f"Not available mods: {not_available_mods}")
# Pourcentage round to 1 decimals
print(f"Percentage: {round(available_mods / (available_mods + not_available_mods) * 100, 1)}%")

pause()
