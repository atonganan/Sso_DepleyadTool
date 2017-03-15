import GetInfo,commands,Tips

def Deployed_Fastdfs_Tomcat():
    print Tips.Deployed_Fastdfs_TomcatTips
    SamplePort=commands.getoutput("cat /apps/sh/fastdfs-jar.sh |grep runport=")
    PortList = GetInfo.GetPortList()
    Ports = str(PortList[0][0])
    ReplacePort = "sed -i  \"s/"+SamplePort+"/runport=("+Ports+")/g\" /apps/sh/fastdfs-jar.sh"
    commands.getoutput(ReplacePort)