import requests
from config.config import config
from src.verify_mod import verify_mod

def verify_pack(pack_version_id, verified_version) -> bool:
    data = requests.get('https://api.modrinth.com/v2/version/{id}'.format(id=pack_version_id)).json()
    dependencies: list = data['dependencies']
    dependency: dict
    available: int = 0
    missing: int = 0
    for dependency in dependencies:
        # If dependency has project_id
        if 'project_id' in dependency.keys():
            project_id: str = dependency['project_id']
            # If null, skip
            if project_id is None:
                print(f"Verify manually for {dependency['file_name']}")
                continue
            # If not, verify
            verified, title = verify_mod(project_id, verified_version)
            if not verified:
                print('Missing: {id}'.format(id=title))
                missing += 1
            else:
                available += 1
                if not config.only_display_missings:
                    print('Found: {id}'.format(id=title))
    print('Available: {available}'.format(available=available))
    print('Missing: {missing}'.format(missing=missing))
    print("Pourcentage available: {pourcentage}%".format(pourcentage=available/(available+missing)*100))