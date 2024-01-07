#!/usr/bin/env python3
import sys
from src.verify_pack import verify_pack

# Get args
args = sys.argv

# Get only the true args
args = args[1:]

# Should have at least one arg
if len(args) != 2:
    print("No pack version and version to verify given")
    exit(1)

verify_pack(args[0], args[1])
