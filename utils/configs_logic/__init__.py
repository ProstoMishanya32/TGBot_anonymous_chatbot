from . import button_config
from . import text_config
from . import yaml_config

common_text = text_config.CommonText()
ru_text = text_config.RuText()

ru_button = button_config.RuButton()

config_manager = yaml_config.ConfigManager("./data/config.yaml")