# parse the ipv4 packet header
def ipv4_parser(buff: str):
    try:
        buff_hex = buff.hex()
    except Exception as e:
        print("The buffer is invalid (check format)")
        raise e

    # Parse the IPv4 header
    # The IPv4 header is 20 bytes long
    # Each field is of a specific size within the header

    # Extract the first byte which contains both version and header length
    version_header_length_byte = int(buff_hex[0:2], 16)
    version = version_header_length_byte >> 4
    header_length = (version_header_length_byte & 0x0F) * 4  
    tos = int(buff_hex[2:4], 16)
    total_length = int(buff_hex[4:8], 16)
    identification = int(buff_hex[8:12], 16)
    # Flags and Fragment Offset
    flags_fragment_offset = int(buff_hex[12:16], 16)
    flags = (flags_fragment_offset & 0xE000) >> 13
    fragment_offset = flags_fragment_offset & 0x1FFF
    ttl = int(buff_hex[16:18], 16)
    protocol = int(buff_hex[18:20], 16)
    header_checksum = buff_hex[20:24]
    source_ip = '.'.join(str(int(buff_hex[i:i+2], 16)) for i in range(24, 32, 2))
    destination_ip = '.'.join(str(int(buff_hex[i:i+2], 16)) for i in range(32, 40, 2))
    ipv4_header = {
        "version": version,
        "header_length": header_length,
        "tos": tos,
        "total_length": total_length,
        "identification": identification,
        "flags": flags,
        "fragment_offset": fragment_offset,
        "ttl": ttl,
        "protocol": protocol,
        "header_checksum": header_checksum,
        "source_ip": source_ip,
        "destination_ip": destination_ip
    }

    return ipv4_header

def print_ipv4_header_info(packet: str):
    # Parse the IPv4 header
    ipv4_header = ipv4_parser(packet)

    # Print IPv4 header information
    print("IPv4 Header Information:")
    print("------------------------")
    print(f"Version: {ipv4_header['version']}")
    print(f"Header Length: {ipv4_header['header_length']} bytes")
    print(f"Type of Service (TOS): {ipv4_header['tos']}")
    print(f"Total Length: {ipv4_header['total_length']} bytes")
    print(f"Identification: {ipv4_header['identification']}")
    print(f"Flags: {ipv4_header['flags']}")
    print(f"Fragment Offset: {ipv4_header['fragment_offset']}")
    print(f"Time to Live (TTL): {ipv4_header['ttl']}")
    print(f"Protocol: {ipv4_header['protocol']}")
    print(f"Header Checksum: {ipv4_header['header_checksum']}")
    print(f"Source IP Address: {ipv4_header['source_ip']}")
    print(f"Destination IP Address: {ipv4_header['destination_ip']}")


