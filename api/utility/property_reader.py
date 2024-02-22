import os

from jproperties import Properties


class PropertyReader:
    current_dir = os.getcwd()
    # Get the parent directory
    parent_dir = os.path.dirname(current_dir)
    CONFIG_PROP_PATH = parent_dir + "\\config.properties"
    config_prop = Properties()

    @classmethod
    def load_config_prop(cls):
        with open(cls.CONFIG_PROP_PATH, 'rb') as config_file:
            cls.config_prop.load(config_file)

    @classmethod
    def load_all_props(cls):
        cls.load_config_prop()