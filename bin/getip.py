from subprocess import run,PIPE
from uuid import getnode
from socket import gethostname ,gethostbyname,gethostbyaddr
from .config import read
def get_ip():
    goat = read("./scapegoat.json")["list"]
    if not isinstance(goat,list):
        goat = [goat]
    # 获取本机IP地址
    my_ip = gethostbyname(gethostname())

    # 执行arp -a命令，获取ARP缓存表
    output = run("arp -a", stdout=PIPE, stderr=PIPE, text=True).stdout.splitlines()

    # 查找包含本机IP地址的接口部分，并确定该部分的范围
    interface_start = None
    interface_end = None
    for index, line in enumerate(output):
        if "接口" in line:
            if my_ip in line:  # 确定包含本机IP的接口起始行
                interface_start = index
            elif interface_start is not None and interface_end is None:  # 确定接口结束行
                interface_end = index
                break

    # 如果找到了相关接口部分，提取该接口下的ARP表项
    arp_table = []
    if interface_start is not None:
        # 如果没有明确的接口结束行，则收集到输出的末尾
        interface_end = interface_end or len(output)
        for line in output[interface_start + 1:interface_end]:
            if line.strip():  # 避免收集空行
                arp_table.append(line)
    # 得到的IP和MAC列表
    ip = [my_ip]
    mac = [':'.join([format((getnode() >> elements) & 0xff, '02x') for elements in range(2, 14, 2)][::-1])]
    for i in arp_table:
        if "动态" in i:
            temp = i.split()
            ip += [temp[0]]
            mac += [temp[-2]]

    name = []
    # 得到名字列表
    for i in ip:
        if gethostbyaddr(i)[0] == "bogon":
            name += [i.split(".")[-2]+"."+i.split(".")[-1]]
        else:
            name += [gethostbyaddr(i)[0]]

    # 替罪羊补足
    for i in goat:
        mac += [i]
        name += ["Goat" + str(int(goat.index(i)) + 1)]
    return ip,mac,name
