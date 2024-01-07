from dacite import from_dict

from dataclasses import dataclass

import json

from src.const import Paths

@dataclass
class Config:
    only_display_missings: bool

def load_config(config_path: str) -> Config:
    with open(config_path, 'r') as f:
        config = json.load(f)
    return from_dict(data_class=Config, data=config)

try:
    config = load_config(Paths.INTERNAL_CONFIG)
except FileNotFoundError:
    print("Config file not found. Be sure execute setup.py first.")