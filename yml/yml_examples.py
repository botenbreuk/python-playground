from pathlib import Path

from main import example, log

import yaml


@example
def read_yaml_file():
    # Read a YAML file and log its contents
    path = Path(__file__).parent / "example.yml"
    with open(path, "r") as file:
        data = yaml.safe_load(file)
        log.info(f"YAML file contents: {data}")
