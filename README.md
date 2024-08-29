# Ping Monitor

## Overview

This project is a ping monitoring tool that continuously pings specified IP addresses, parses the results, and exports the metrics to Prometheus. These metrics can then be visualized in Grafana. The tool is designed to run indefinitely, providing real-time monitoring of network performance and reliability.

## Metrics

The following metrics are collected and exported to Prometheus:

- **Packet Transmit**: Number of packets transmitted.
- **Packet Receive**: Number of packets received.
- **Packet Loss Rate**: Percentage of lost packets.
- **RTT Min**: Minimum round-trip time in milliseconds.
- **RTT Avg**: Average round-trip time in milliseconds.
- **RTT Max**: Maximum round-trip time in milliseconds.
- **RTT Mdev**: Population standard deviation of round-trip time.
- **Ping Success Rate**: Percentage of successful pings.

## Requirements

- Python 3.x
- `pingparsing` library
- `PyYAML` library
- `prometheus_client` library
- Prometheus and Grafana for metrics collection and visualization

## Installation

1. Clone the repository:
    ```bash
    git clone <https://github.com/bryantolmos/Ping-Monitor.git>
    ```

2. Install the required Python packages:
    ```bash
    pip install pingparsing pyyaml prometheus_client
    ```

3. Set up Prometheus and Grafana (refer to their respective documentation for installation).

## Configuration

Create a YAML configuration file (e.g., `config.yaml`) with the following structure:

```yaml
address1:
  ip: "192.168.1.1"
  frequency: 1  # Ping frequency in seconds

address2:
  ip: "8.8.8.8"
  frequency: 1

# Add more addresses as needed
```
## Usage

### 1. Starting our program.
To start the ping monitor run the `start()` function, which can be done like this:
```python
import pingmonitor

def main():
    config_file = "config.yaml"
    pingmonitor.start(config_file)

if __name__ == "__main__":
    main()
```
this will not only start the ping monitor, but it will expose the metrics to port `8989`(default port), which will be scraped by promtheus. 

### 2. Starting prometheus
Next, start the Prometheus database to scrape the data from our program. Ensure that localhost:8989 is added to the prometheus.yml file under static_configs. Once Prometheus is installed and set up, start it with the following command in the terminal:
```shell 
 ./prometheus --config.file=prometheus.yml
```
### 3. Starting graphana
Lastly to visualize our data we must start graphana by running the following command (dependent on OS)
```shell
brew services start grafana-agent
```

## Visualization

Once prometheus is set up to scrape the metrics, We use Graphana dashboards to visualize the collected metric which looks like:
<img width="1440" alt="Screenshot 2024-08-29 at 11 16 21 AM" src="https://github.com/user-attachments/assets/4dcee3ac-2dc8-457d-ad78-b3ebcd4a88c4">

## Conclusion
This ping monitoring tool provides a comprehensive solution for real-time monitoring of network performance. With easy integration into Prometheus and Grafana, you can visualize and analyze network metrics to ensure your infrastructure is running smoothly

