import pingparsing

def ping_parse(ping_destination : str, ping_count : int) -> tuple[dict,list]:

    """
    Pings a host and returns a list of the ping results and ICMP replies

    Arguements: 
        ping_destination (str): the host name or IP address to ping
        ping_count (int): the amount of pings to send

    Returns:

    """

    ping_parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination = ping_destination
    transmitter.count = ping_count

    # initialize ping_results and icmp_replies_list
    ping_results = ping_parser.parse(transmitter.ping())
    icmp_replies_list = []

    # iterate over ICMP replies and append to list
    for icmp_replies in ping_results.icmp_replies:
        icmp_replies_list.append(icmp_replies)

    # optional save as json -----------------------------

    #with open('ping_results.json', 'w') as file:
    #    json.dump(ping_results.as_dict(), file, indent=4)
    #with open('icmp_replies.json', 'w') as file:
    #    json.dump(icmp_replies_list, file, indent=4)
    
    # ---------------------------------------------------
    
    
    return ping_results.as_dict(), icmp_replies_list
