import os
import yaml
from yaml.loader import SafeLoader


class FileReadError(Exception):
    """Custom exception for file read errors."""
    pass


class YAMLParseError(Exception):
    """Custom exception for YAML parsing errors."""
    pass


def load_code_content(file_path):
    """Helper function to load content from the selected file."""
    if not os.path.exists(file_path):
        raise FileReadError(f"Error: File not found at {file_path}")

    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            if not content:
                raise FileReadError(f"File is empty: {file_path}")
            return content
    except FileNotFoundError as fnf_error:
        raise fnf_error
    except PermissionError as perm_error:
        raise perm_error
    except Exception as e:
        raise FileReadError(
            f"An unexpected error occurred while reading the file: {file_path}: {str(e)}")


def load_yaml_config(file_path):
    """Helper function to load YAML configuration from the selected file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: File not found at {file_path}")

    try:
        with open(file_path, 'r') as file:
            config = yaml.load(file, Loader=SafeLoader)
            if config is None:
                raise YAMLParseError(f"YAML file is empty or invalid: {file_path}")
            return config
    except FileNotFoundError as fnf_error:
        raise fnf_error
    except PermissionError as perm_error:
        raise perm_error
    except yaml.YAMLError as yaml_error:
        raise YAMLParseError(f"YAML parsing error in file {file_path}: {str(yaml_error)}")
    except Exception as e:
        raise Exception(
            f"An unexpected error occurred while loading the YAML file: {file_path}: {str(e)}")
