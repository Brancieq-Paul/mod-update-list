import json
from src.const import Paths
from config.config import config

class InstanceFile:

    # List of all instance files
    instance_files = []

    # Init with instance file json:
    # {
    #    "projectID",
    #    "fileID",
    #    "required"
    # }
    def __init__(self, instance_file_json: dict):
        self.project_id = instance_file_json["projectID"]
        self.file_id = instance_file_json["fileID"]
        self.required = instance_file_json["required"]

    # Add instance file to list
    @staticmethod
    def add_instance_file(instance_file: dict):
        InstanceFile.instance_files.append(InstanceFile(instance_file))

    # Load all instance files from minecraftinstance.json
    @staticmethod
    def load_instance_files():
        with open(config.cf_pack_path + Paths.MINECRAFT_INSTANCE_JSON, 'r') as f:
            instance = json.load(f)
        for instance_file in instance["manifest"]["files"]:
            InstanceFile.add_instance_file(instance_file)