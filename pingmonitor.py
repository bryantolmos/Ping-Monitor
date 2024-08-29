import yaml
import pingparsing
import os
import time
import concurrent.futures
from prometheus_client import start_http_server, Gauge

# initialize metrics with server label - global
packet_transmit = Gauge("packet_transmit", "packets transmitted",["server"])
packet_receive = Gauge("packet_receive", "packets received",["server"])
packet_loss_rate = Gauge("packet_loss_rate", "packet loss rate",["server"])
rtt_min = Gauge("rtt_min", "round trip time min in milliseconds",["server"])
rtt_avg = Gauge("rtt_avg", "round trip time avg in milliseconds",["server"])
rtt_max = Gauge("rtt_max", "round trip time max in milliseconds",["server"])
rtt_mdev = Gauge("rtt_mdev", "round trip time population standard deviation",["server"])
ping_success_rate = Gauge("ping_success_rate", "Ping success rate", ["server"])

def parse_yaml(yaml_file_name: str) -> dict:
    print(f"Looking for YAML file at: {os.path.abspath(yaml_file_name)}")
    try:
        with open(yaml_file_name, 'r') as file:
            yaml_file_contents = yaml.safe_load(file)
            return yaml_file_contents
    except FileNotFoundError:
        raise FileNotFoundError(f"\n\nYAML file not found: {yaml_file_name}\n")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"\n\nSyntax error in YAML file: {yaml_file_name} - {e}\n")
    except Exception as e:
        raise Exception(f"\n\nAn error occurred while reading the YAML file: {e}\n")

def ping_parse(ping_destination : str, frequency: int) -> None:
    ping_parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination = ping_destination

    successful_pings = 0
    total_pings = 0

    while True:
        ping_results = ping_parser.parse(transmitter.ping())
        icmp_replies_list = ping_results.icmp_replies

        total_pings += 1
        if ping_results.packet_receive > 0:
            successful_pings += 1

        ping_data = {
            "ping_results": {
                "packet_transmit": ping_results.packet_transmit,
                "packet_receive": ping_results.packet_receive,
                "packet_loss_rate": ping_results.packet_loss_rate,
                "rtt_min": ping_results.rtt_min,
                "rtt_avg": ping_results.rtt_avg,
                "rtt_max": ping_results.rtt_max,
                "rtt_mdev": ping_results.rtt_mdev,
            },  
            "icmp_replies": icmp_replies_list
        }

        # set the metric values
        packet_transmit.labels(server=ping_destination).set(ping_data["ping_results"]["packet_transmit"])
        packet_receive.labels(server=ping_destination).set(ping_data["ping_results"]["packet_receive"])
        packet_loss_rate.labels(server=ping_destination).set(ping_data["ping_results"]["packet_loss_rate"])
        rtt_min.labels(server=ping_destination).set(ping_data["ping_results"]["rtt_min"])
        rtt_max.labels(server=ping_destination).set(ping_data["ping_results"]["rtt_max"])
        rtt_avg.labels(server=ping_destination).set(ping_data["ping_results"]["rtt_avg"])
        rtt_mdev.labels(server=ping_destination).set(ping_data["ping_results"]["rtt_mdev"])

        success_rate = (successful_pings/total_pings)*100
        ping_success_rate.labels(server=ping_destination).set(success_rate)

        time.sleep(frequency)

def caller(config_yaml : str) -> None:
    script_dir = os.path.dirname(__file__)  # Get the directory where the script is located
    config_yaml_path = os.path.join(script_dir, config_yaml)  # Build the full path
    config_contents = parse_yaml(config_yaml_path)

    def worker(ip, frequency):
        ping_parse(ip, frequency)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(1, len(config_contents)+1):
            ip = config_contents[f'address{i}']['ip']
            frequency = config_contents[f'address{i}']['frequency']
            executor.submit(worker, ip, frequency)

def start(config_yaml : str) -> None:
    start_http_server(8989)
    caller(config_yaml)
