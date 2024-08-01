import yaml
import yaml.scanner

def read_yaml(yaml_file_name: str, print_yaml : bool) -> dict:
    """
    Reads a YAML file and returns its contents as a dictionary.

    Parameters:
    yaml_file_name (str): The path to the YAML file.

    Returns:
    dict: The contents of the YAML file as a dictionary.

    Raises:
    FileNotFoundError: If the file does not exist.
    yaml.YAMLError: If there is an error in the YAML syntax.
    Exception: For any other exceptions that occur.
    """
    try:
        with open(yaml_file_name, 'r') as file:
            yaml_file = yaml.safe_load(file)
            if print_yaml == True:
                for keys in yaml_file:
                    print(f"{keys} : {yaml_file[keys]}")
            return yaml_file

    except FileNotFoundError:
        raise FileNotFoundError(f"\n\nYAML file not found: {yaml_file_name}\n")

    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"\n\nSyntax error in YAML file: {yaml_file_name} - {e}\n")

    except Exception as e:
        raise Exception(f"\n\nAn error occurred while reading the YAML file: {e}\n")