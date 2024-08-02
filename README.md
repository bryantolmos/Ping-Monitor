# Ping Monitor - Bryant Olmos


## ping_parse.py
### ping_parse()
* Pings a host and prints ping results along with ICMP replies
* #### Arguements:
   - `ping_destinations : str`: the host name or IP address to ping
* #### Returns:
   - 0 is returned if program executed successfully 



## readYaml.py
### read_yaml()
* Read a YAML file and returns its contents as a dictionary
* #### Arguments:
    - `yaml_file_name : str`: the path to the YAML file
    - `print_yaml : bool`: true to print YAML file contents to terminal false otherwise
* #### Returns:
   - `yaml_file : dict`: the contents of the YAML file as a dictionary
* #### Raises:
    - FileNotFoundError: if the file does not exist
    - yaml.YAMLError: if there is an error in the YAML syntax
    - Exception: for any other exception that occur
