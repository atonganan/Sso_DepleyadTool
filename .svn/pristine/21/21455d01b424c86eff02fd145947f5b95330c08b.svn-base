import commands,time,GetInfo,Tips
def Deployed_java():
    PortList = GetInfo.GetPortList()
    SsoJavaStartCount = input(Tips.SsoJavaStartCountTips)
    if SsoJavaStartCount ==1:
        SamplePort=commands.getoutput("cat /apps/sh/sso-jar.sh |grep runport=")
        Ports = str(PortList[2][0])
        ReplacePort = "sed -i  \"s/"+SamplePort+"/runport=("+Ports+")/g\" /apps/sh/sso-jar.sh"
        commands.getoutput(ReplacePort)
    elif SsoJavaStartCount ==2:
        SamplePort=commands.getoutput("cat /apps/sh/sso-jar.sh |grep runport=")
        Ports = str(PortList[2][0])+" "+str(PortList[2][1])
        ReplacePort = "sed -i  \"s/"+SamplePort+"/runport=("+Ports+")/g\" /apps/sh/sso-jar.sh"
        commands.getoutput(ReplacePort)
    elif SsoJavaStartCount ==3:
        SamplePort=commands.getoutput("cat /apps/sh/sso-jar.sh |grep runport=")
        Ports = str(PortList[2][0])+" "+str(PortList[2][1])+" "+str(PortList[2][2])
        ReplacePort = "sed -i  \"s/"+SamplePort+"/runport=("+Ports+")/g\" /apps/sh/sso-jar.sh"
        commands.getoutput(ReplacePort)
    elif SsoJavaStartCount ==4:
        SamplePort=commands.getoutput("cat /apps/sh/sso-jar.sh |grep runport=")
        Ports = str(PortList[2][0])+" "+str(PortList[2][1])+" "+str(PortList[2][2])+" "+str(PortList[2][3])
        ReplacePort = "sed -i  \"s/"+SamplePort+"/runport=("+Ports+")/g\" /apps/sh/sso-jar.sh"
        commands.getoutput(ReplacePort)
    elif SsoJavaStartCount ==5:
        SamplePort=commands.getoutput("cat /apps/sh/sso-jar.sh |grep runport=")
        Ports = str(PortList[2][0])+" "+str(PortList[2][1])+" "+str(PortList[2][2])+" "+str(PortList[2][3])+" "+str(PortList[2][4])
        ReplacePort = "sed -i  \"s/"+SamplePort+"/runport=("+Ports+")/g\" /apps/sh/sso-jar.sh"
        commands.getoutput(ReplacePort)
    else:
        print Tips.ParameterError
        time.sleep(10)
        exit()
