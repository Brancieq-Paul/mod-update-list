from cursepy import CurseClient
from cursepy.wrapper import base 
from config.config import config

# Create a client
client = CurseClient(config.cf_api_key)

def get_mod(mod_id: int) -> base.CurseAddon:
    addon = client.addon(mod_id)
    return addon

# Verify if the mod exists for the given version
def verify_mod(mod_id: int, versions: str):
    addon = get_mod(mod_id)
    file_list = addon.files()
    asked_version = any(all(version in file.version for version in versions) for file in file_list)
    if asked_version:
        # Print that the mod exists for the given version
        print(f"Mod '{addon.name}' available")
        return True
    else:
        # Print that the mod does not exist for the given version
        print(f"Mod '{addon.name}' is NOT available")
        return False