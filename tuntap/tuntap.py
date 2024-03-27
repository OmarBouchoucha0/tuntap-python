from pytun import TunTapDevice
from ipv4Parser import print_ipv4_header_info

tun = TunTapDevice(name='tun0')
tun.mtu = 1500 # the maximum transion unit (max length of the packet)

if __name__ == "__main__":
    tun.up()
    print("opening tunnel")
    while True:
        try:
            buff = tun.read(tun.mtu)
            flags = buff[:2]
            flags_int = int.from_bytes(flags, byteorder='big')
            protocol = buff[2:4]
            protocol_int = int.from_bytes(protocol, byteorder='big')
            packet = buff[4:]
            if protocol_int == 0x0800:
                print("Ethernet Header Inforamtion :")
                print("flags : " + str(flags_int))
                print("protocol : " + hex(protocol_int) + " (TPC) ")
                print_ipv4_header_info(packet)
                print(50*"*")
        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Exiting...")
            tun.close()
            break                                      
        except:
            print("something unexpected happend")
            break
