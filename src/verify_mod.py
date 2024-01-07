import requests

def verify_mod(mod_id, mod_version) -> (bool,str):
    url: str = 'https://api.modrinth.com/v2/project/{id}'
    data: dict = requests.get(url.format(id=mod_id)).json()
    projectType: str = data['project_type']
    if projectType != 'mod':
        raise Exception('Invalid project type: {type}'.format(type=projectType))
    game_versions: list = data['game_versions']
    if mod_version not in game_versions:
        return (False, data['title'])
    return (True, data['title'])