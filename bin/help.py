def help(list):
    if len(list) == 0:
        print("new   新建替罪羊")
        print("del   删除替罪羊")
        print("let   新建一个任务")
        print("stop  停止一个任务")
        print("host  解析计算机名")
        print("exit  退出程序")

    else:
        if list[0] == "help":
            print("help [command]")
            print("command - 显示该命令的帮助信息")
        elif list[0] == "new":
            print("新建替罪羊{有MAC没IP}")
        elif list[0] == "del":
            print("del [Goat]")
            print("删除替罪羊")
            print("Goat为数字")
        elif list[0] == "let":
            print("let [(except) hosts] think [ip] is [mac]")
            print("新建一个任务")
            print("except 除去")
            print("hosts 在有except可以不写")
            print("例:")
            print("   let except 0.103 0.102 think 0.101 is Goat3")
            print("   让除0.103 0.102 认为0.101的MAC是替罪羊3")
            print("当然，其实有些不重要的单词没拼对也可以")
        elif list[0] == "stop":
            print("stop [(except) num]")
            print("停止一个任务")
            print("也支持except")
        elif list[0] == "host":
            print("host [hostname]")
            print("解析Hostname的IP或名称")
            print("用于无法通过IP解析计算机名的时候")
        elif list[0] == "exit":
            print("退出程序")
