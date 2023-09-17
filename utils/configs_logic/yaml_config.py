import yaml

class ConfigManager:
    def __init__(self, filename):
        self.filename = filename
        self.load_config()

    def load_config(self):
        try:
            with open(self.filename, "r") as yaml_file:
                self.config = yaml.safe_load(yaml_file)
        except FileNotFoundError:
            self.config = {}

    def save_config(self):
        with open(self.filename, "w") as yaml_file:
            yaml.dump(self.config, yaml_file, default_flow_style=False)

    def get_value(self, key, default=None):
        return self.config.get(key, default)

    def set_value(self, key, value):
        self.config[key] = value
        self.save_config()



