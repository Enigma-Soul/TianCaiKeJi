from random import randint
def ranmac():
    mac = [randint(0x00, 0xff) for _ in range(6)]
    mac_address = ":".join(f"{x:02x}" for x in mac)
    return mac_address
