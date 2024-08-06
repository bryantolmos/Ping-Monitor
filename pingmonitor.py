import yaml
import pingparsing
import os
import concurrent.futures

def parse_yaml(yaml_file_name: str) -> dict:
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

def ping_parse(ping_destination : str, ping_count : int) -> str:
    ping_parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination = ping_destination
    transmitter.count = ping_count

    ping_results = ping_parser.parse(transmitter.ping())
    icmp_replies_list = ping_results.icmp_replies

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

    base_file_name = f"ping_results_{ping_destination.replace('.', '_')}"
    output_file = f"{base_file_name}.yaml"

    counter = 1
    while os.path.exists(output_file):
        output_file = f"{base_file_name}_{counter}.yaml"
        counter += 1

    with open(output_file, 'w') as file:
        yaml.dump(ping_data, file)

    return output_file

def caller(config_yaml : str) -> None:
    config_contents = parse_yaml(config_yaml)
    
    def worker(ip, count):
        ping_parse(ip, count)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(1, len(config_contents)+1):
            ip = config_contents[f'address{i}']['ip']
            count = config_contents[f'address{i}']['count']
            futures.append(executor.submit(worker, ip, count))

        concurrent.futures.wait(futures)