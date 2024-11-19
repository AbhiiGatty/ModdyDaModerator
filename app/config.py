import yaml
import os

class Config:
    """Global configuration manager."""
    _config = None  # Private variable to store the loaded configuration

    @classmethod
    def load_config(cls, filepath: str):
        """
        Load the YAML configuration from a file.
        :param filepath: Path to the YAML configuration file.
        :raises FileNotFoundError: If the file does not exist.
        :raises RuntimeError: If the configuration file cannot be parsed.
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Configuration file not found: {filepath}")

        try:
            with open(filepath, 'r') as file:
                cls._config = yaml.safe_load(file)
        except yaml.YAMLError as e:
            raise RuntimeError(f"Failed to parse configuration file: {e}")

    @classmethod
    def get(cls, key: str, default=None):
        """
        Retrieve a configuration value.
        :param key: Dot-separated key to access nested configurations (e.g., 'credentials.usernames').
        :param default: Default value if the key is not found.
        :return: Configuration value or default.
        """
        if cls._config is None:
            raise RuntimeError("Configuration not loaded. Call `load_config` first.")

        keys = key.split('.')
        value = cls._config
        try:
            for k in keys:
                value = value[k]
        except (KeyError, TypeError):
            return default
        return value
