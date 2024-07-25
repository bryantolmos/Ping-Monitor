import yaml
import yaml.scanner

# Path to yaml file
yaml_file_name = "sample.yaml"

try:
    with open(yaml_file_name, 'r') as file:
        yaml_file = yaml.safe_load(file)

    print("Yaml File Contents:")
    for keys in yaml_file:
        print(f"{keys} : {yaml_file[keys]}")
except yaml.scanner.ScannerError:
    print("\n## Syntax Error In Yaml File  ##\n## Scanner Error In Yaml File ##\n")
except FileNotFoundError:
    print("\n## Yaml File Not Found    ##\n## Or File Does Not Exits ##\n")
except Exception as e:
    print(f"\n## Error: {e} ##\n")
