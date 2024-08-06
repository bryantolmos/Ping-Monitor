# Ping Monitor
## Overview
This program uses a YAML configuration file containing IP addresses and the amount of times to ping that target IP, the program performs ping test on each IP, saves the results to a yaml file, while using concurrent execution to handle multiple ping test, improving efficiency for large configurations

## Usage
### 1. Preparing a YAML Configuration File
To set up your configuration file, follow these steps:

- **Address Keywords:** Define the target addresses by using keywords formatted as `address` followed by a unique identifier (e.g., numbers 1 to n).
  - _Example:_ `address1:`
- **IP Address Specification:** For each `address` keyword, specify the corresponding IP address of the target using the `ip` key.
  - _Example:_ `ip: 8.8.8.8`
- **Ping Count Configuration:** Lastly, set the number of pings to be sent to the target by including a `count` key with the desired value.
  - _Example:_ `count: 5`
 
Assuming all steps were followed correctly your YAML configuration file should look like this
```yaml
address1:
   ip: 8.8.8.8
   count: 5
address2:
   ip: 1.1.1.1
   count: 4
```
 
### 2. Running the program 
To run the program, follow these steps:
- **Install required libraries:** Can be done with the following commands
  ```
  pip install pingparsing
  ```
  ```
  pip install pyyaml
  ```
- **Call the function:** Use `caller()` and input your YAML configuration file
  ```python
  import pingmonitor
  
  pingmonitor.caller('config.yaml')
  ```
### 3. Results
The program will generate YAML files containing ping results and ICMP replies for each IP address in the YAML configuration file, these files will be saved in the same directory where the scripts is executed
