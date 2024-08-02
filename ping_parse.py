import pingparsing

def ping_parse(ping_destination : str, ping_count : int) -> int:
    ping_parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination = ping_destination
    transmitter.count = ping_count

    ping_results = ping_parser.parse(transmitter.ping())
    icmp_replies_list = ping_results.icmp_replies

    print(f"\nPing Results for {ping_destination}:")
    print("-" * 40)
    print(f"Packet Transmitted: {ping_results.packet_transmit}")
    print(f"Packet Received: {ping_results.packet_receive}")
    print(f"Packet Loss: {ping_results.packet_loss_rate:.2f}%")
    print(f"Round Trip Time (ms):")
    print(f"  Min: {ping_results.rtt_min:.2f}")
    print(f"  Avg: {ping_results.rtt_avg:.2f}")
    print(f"  Max: {ping_results.rtt_max:.2f}")
    print(f"  Mdev: {ping_results.rtt_mdev:.2f}")

    print("\nICMP Replies:")
    print("-" * 40)
    for i, reply in enumerate(icmp_replies_list, start=1):
        print(f"Reply {i}:")
        print(f"  Destination: {reply['destination']}")
        print(f"  Bytes: {reply['bytes']}")
        print(f"  Sequence: {reply['icmp_seq']}")
        print(f"  TTL: {reply['ttl']}")
        print(f"  Time (ms): {reply['time']:.2f}")
        print(f"  Duplicate: {reply['duplicate']}")
        print("-" * 40)
    
    return 0