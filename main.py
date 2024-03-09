from bin import *
from kernel import kernel
from threading import Thread
from time import sleep
from sys import exit
from socket import gethostbyname,gethostbyaddr
"""运行后台指令发送程序"""
class RunningThread(Thread):
    def __init__(self):
        super().__init__()
        self.stop_signal = False
    def run(self):
        while not self.stop_signal:
            kernel()
            sleep(2)
    def stop(self):
        self.stop_signal = True


def run(command):
    if command[0] == "new":
        while True:
            ran = ranmac()
            if ran not in mac and ran not in read("./scapegoat.json")["list"]:
                break
        goat = read("./scapegoat.json")["list"]
        if not isinstance(goat,list):
            goat = [goat]
        write("./scapegoat.json",{"list":goat+[ran]})
    elif command[0] == "del":
        try:
            goat = read("./scapegoat.json")["list"]
            if not isinstance(goat,list):
                goat = [goat]
            write("./scapegoat.json",{"list":goat.pop(int(int(command[1])-1))})
        except:
            print("列表错误")
    elif command[0] == "let":
        try:
            reads = read("./running.json")
            forc = command[1:-4]
            if forc[0] == "except":
                excep = True
                forc.pop(0)
            else:
                excep = False
            for i in range(len(forc)):
                forc[i] = ip[name.index(forc[i])]
            w_ip = command[-3]
            w_ip = ip[name.index(w_ip)]
            w_mac = command[-1]
            w_mac = mac[name.index(w_mac)]
            num = int(reads["number"]) + 1
            if excep:
                temp = {"except": "True", "for": forc, "ip": w_ip, "mac": w_mac}
            else:
                temp = {"except": "False", "for": forc, "ip": w_ip, "mac": w_mac}

            reads.update({str(num): temp})
            reads.update({"number":num})
            for i in range(3):
                write("./running.json", reads)
                sleep(0.1)
        except Exception as a:
            print("命令错误")
    elif command[0] == "stop":
        try:
            reads = read("./running.json")
            if int(command[1]) > reads["number"]:
                print("无效的数字")
            else:
                reads.pop(str(int(command[1])))
                for i in range(int(command[1])-reads["number"]):
                    poo = reads.pop(str(int(int(reads["number"])-i)))
                    reads += {str(int(int(reads["number"])-i-1))+"a" : poo}
                for i in range(int(command[1]) - reads["number"]):
                    poo = reads.pop(str(int(int(reads["number"]) - i))+"a")
                    reads += {str(int(int(reads["number"]) - i)) : poo}
                # 更改number
                reads["number"] = reads["number"] - 1
            # 写入
            for i in range(3):
                write("./running.json", reads)
                sleep(0.1)
        except:
            print("非数字")
    elif command[0] == "help":
        help(command[1:])
    elif command[0] == "host":
        try:
            t_ip = gethostbyname(command[1])
            if gethostbyaddr(t_ip)[0] == "bogon":
                print(t_ip.split(".")[-2]+"."+t_ip.split(".")[-1])
            else:
                print(gethostbyaddr(t_ip)[0])
        except:
            print(str(command[1])+"并不是个计算机名")
    elif command[0] == "exit":
        Run.stop()
        exit(0)
    else:
        print(command[0]+" is not a command")

def output():
    # 打印局域网
    print(color("green","/"),end="")
    for i in name:
        if "Goat" in i:
            print(color("yellow",i),end="")
            print(color("green","/"),end="")
        else:
            print(color("blue",i),end="")
            print(color("green","/"),end="")
    print("")
    # 打印任务
    reads = read("./running.json")
    for i in range(int(reads["number"])):
        print(color("green",str(i+1)+" 让"),end="")
        if reads[str(i+1)]["except"] == "True":
            print(color("red","除去"),end="")
        forc = reads[str(i+1)]["for"]
        if forc[0] == str(forc[0]):
            forc = [forc]
        for x in forc:
            if x[0] in ip:
                print(color("yellow",name[ip.index(x[0])]),end="")
            else:
                print(color("yellow","???"),end="")
            print(" ",end="")
        print(color("green","认为"),end="")
        if reads[str(i+1)]["ip"] in ip:
            print(color("yellow",name[ip.index(reads[str(i+1)]["ip"])]),end="")
        else:
            print(color("yellow","???"),end="")
        print(color("green","的Mac是"),end="")
        if reads[str(i+1)]["mac"] in mac:
            print(color("yellow",name[mac.index(reads[str(i+1)]["mac"])]),end="")
        else:
            print(color("yellow","???"),end="")
        print("")
if __name__ == "__main__":
    Run = RunningThread()
    Run.start()
    while True:
        clear()
        ip, mac, name = get_ip()
        output()
        inp = input(color("blue","->#")).split(" ")
        if inp == ['']:
            pass
        elif inp == "exit":
            run(inp)
            break
        else:
            run(inp)
            input("按Enter键重置")
