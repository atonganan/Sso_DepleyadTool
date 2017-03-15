import commands,GetInfo,Tips
def Deployed_Fastdfs_Tomcat(): 
    print Tips.Deployed_Fastdfs_TomcatTips
    PortList = GetInfo.GetPortList()
    commands.getoutput("mkdir -p /apps/conf/tomcat_fastdfs/"+str(PortList[1][0]))
    commands.getoutput("mkdir -p /apps/logs/tomcat_fastdfs/"+str(PortList[1][0]))
    commands.getoutput("cp -rf /apps/svr/tomcat_fastdfs/apache-tomcat-7.0.70_8116 /apps/svr/tomcat_fastdfs/apache-tomcat-7.0.70_"+str(PortList[1][0]))
    commands.getoutput("ln -s /apps/svr/tomcat_fastdfs/apache-tomcat-7.0.70_"+str(PortList[1][0])+" /apps/svr/tomcat_fastdfs/tomcat_"+str(PortList[1][0]))
    commands.getoutput("cp -rf  /apps/conf/tomcat_fastdfs/8116/* /apps/conf/tomcat_fastdfs/"+str(PortList[1][0]))
    commands.getoutput("ln -s /apps/conf/tomcat_fastdfs/"+str(PortList[1][0])+" /apps/svr/tomcat_fastdfs/tomcat_"+str(PortList[1][0])+"/conf")
    commands.getoutput("sed -i  \'s/port=\"18030\"/port=\""+str(PortList[3][1])+"\"/g\' /apps/conf/tomcat_fastdfs/"+str(PortList[1][0])+"/server.xml")
    commands.getoutput("ln -s /apps/logs/tomcat_fastdfs/"+str(PortList[1][0])+" /apps/svr/tomcat_fastdfs/tomcat_"+str(PortList[1][0])+"/logs")
    commands.getoutput("rm -rf /apps/svr/tomcat_fastdfs/apache-tomcat-7.0.70_"+str(PortList[1][0])+"/webapps")
    commands.getoutput("ln -s /apps/dat/javadat/default/service-consumer/fastdfs/"+str(PortList[1][0])+" /apps/svr/tomcat_fastdfs/tomcat_"+str(PortList[1][0])+"/webapps")
    SamplePort=commands.getoutput("cat /apps/sh/fastdfs-tomcat.sh |grep runport=")
    Ports = str(PortList[1][0])
    ReplacePort = "sed -i  \"s/"+SamplePort+"/runport=("+Ports+")/g\" /apps/sh/fastdfs-tomcat.sh"
    commands.getoutput(ReplacePort)