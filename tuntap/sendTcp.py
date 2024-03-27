import socket

def send_tcp_packet(destination_ip, destination_port, data):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("socket created")
        s.connect((destination_ip, destination_port))
        print("socket connected")
        s.sendall(data.encode())
        print("socket sent")
        s.close()
        print("TCP packet sent successfully.")
    except Exception as e:
        print(f"Failed to send TCP packet: {e}")


if __name__ == "__main__":
    destination_ip = "192.168.1.18"
    destination_port = 80
    data = "hello world"
    send_tcp_packet(destination_ip, destination_port, data)
