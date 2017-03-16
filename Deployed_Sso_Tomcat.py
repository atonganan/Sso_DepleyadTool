import commands,GetInfo,time,Tips
def Deployed_Sso_Tomcat():
    PortList =GetInfo.GetPortList()
    SsoTomcatStartCount = input(Tips.SsoTomcatStartCountTips)
    if SsoTomcatStartCount == 1:
        commands.getoutput("mkdir -p /apps/conf/tomcat_sso/"+str(PortList[3][0]))
        commands.getoutput("mkdir -p /apps/logs/tomcat_sso/"+str(PortList[3][0]))
        commands.getoutput("cp -rf /apps/svr/tomcat_sso/apache-tomcat-7.0.70_8105 /apps/svr/tomcat_sso/apache-tomcat-7.0.70_"+str(PortList[3][0]))
        commands.getoutput("ln -s /apps/svr/tomcat_sso/apache-tomcat-7.0.70_"+str(PortList[3][0])+" /apps/svr/tomcat_sso/tomcat_"+str(PortList[3][0]))
        commands.getoutput("cp -rf  /apps/conf/tomcat_sso/8105/* /apps/conf/tomcat_sso/"+str(PortList[3][0]))
        commands.getoutput("ln -s /apps/conf/tomcat_sso/"+str(PortList[3][0])+" /apps/svr/tomcat_sso/tomcat_"+str(PortList[3][0])+"/conf")
        commands.getoutput("sed -i  \'s/port=\"8105\"/port=\""+str(PortList[3][0])+"\"/g\' /apps/conf/tomcat_sso/"+str(PortList[3][0])+"/server.xml")
        commands.getoutput("sed -i  \'s/port=\"18030\"/port=\""+str(PortList[3][1])+"\"/g\' /apps/conf/tomcat_sso/"+str(PortList[3][0])+"/server.xml") #zhifeng
        commands.getoutput("sed -i  \'s/port=\"28034\"/port=\""+str(PortList[3][2])+"\"/g\' /apps/conf/tomcat_sso/"+str(PortList[3][0])+"/server.xml") #zhifeng
        commands.getoutput("ln -s /apps/logs/tomcat_sso/"+str(PortList[3][0])+" /apps/svr/tomcat_sso/tomcat_"+str(PortList[3][0])+"/logs")
        commands.getoutput("rm -rf /apps/svr/tomcat_sso/apache-tomcat-7.0.70_"+str(PortList[3][0])+"/webapps")
        commands.getoutput("ln -s /apps/dat/javadat/sso/service-consumer/"+str(PortList[3][0])+" /apps/svr/tomcat_sso/tomcat_"+str(PortList[3][0])+"/webapps") 
        SamplePort=commands.getoutput("cat /apps/sh/sso-tomcat.sh |grep runport=")
        Ports = str(PortList[3][0])
        ReplacePort = "sed -i  \"s/"+SamplePort+"/runport=("+Ports+")/g\" /apps/sh/sso-tomcat.sh"
        commands.getoutput(ReplacePort)              
    elif SsoTomcatStartCount == 2:
        commands.getoutput("mkdir -p /apps/conf/tomcat_sso/{"+str(PortList[3][0])+","+str(PortList[3][3])+"}")
        commands.getoutput("mkdir -p /apps/logs/tomcat_sso/{"+str(PortList[3][0])+","+str(PortList[3][3])+"}")    
        commands.getoutput("cp -rf /apps/svr/tomcat_sso/apache-tomcat-7.0.70_8105 /apps/svr/tomcat_sso/apache-tomcat-7.0.70_"+str(PortList[3][0]))
        commands.getoutput("cp -rf /apps/svr/tomcat_sso/apache-tomcat-7.0.70_8105 /apps/svr/tomcat_sso/apache-tomcat-7.0.70_"+str(PortList[3][3]))
        commands.getoutput("ln -s /apps/svr/tomcat_sso/apache-tomcat-7.0.70_"+str(PortList[3][0])+" /apps/svr/tomcat_sso/tomcat_"+str(PortList[3][0]))
        commands.getoutput("ln -s /apps/svr/tomcat_sso/apache-tomcat-7.0.70_"+str(PortList[3][3])+" /apps/svr/tomcat_sso/tomcat_"+str(PortList[3][3]))
        commands.getoutput("cp -rf  /apps/conf/tomcat_sso/8105/* /apps/conf/tomcat_sso/"+str(PortList[3][0]))
        commands.getoutput("cp -rf  /apps/conf/tomcat_sso/8105/* /apps/conf/tomcat_sso/"+str(PortList[3][3]))
        commands.getoutput("ln -s /apps/conf/tomcat_sso/"+str(PortList[3][0])+" /apps/svr/tomcat_sso/tomcat_"+str(PortList[3][0])+"/conf")
        commands.getoutput("ln -s /apps/conf/tomcat_sso/"+str(PortList[3][3])+" /apps/svr/tomcat_sso/tomcat_"+str(PortList[3][3])+"/conf")    
        commands.getoutput("sed -i  \'s/port=\"8105\"/port=\""+str(PortList[3][0])+"\"/g\' /apps/conf/tomcat_sso/"+str(PortList[3][0])+"/server.xml")
        commands.getoutput("sed -i  \'s/port=\"18030\"/port=\""+str(PortList[3][1])+"\"/g\' /apps/conf/tomcat_sso/"+str(PortList[3][0])+"/server.xml")
        commands.getoutput("sed -i  \'s/port=\"28034\"/port=\""+str(PortList[3][2])+"\"/g\' /apps/conf/tomcat_sso/"+str(PortList[3][0])+"/server.xml")
        commands.getoutput("sed -i  \'s/port=\"8105\"/port=\""+str(PortList[3][3])+"\"/g\' /apps/conf/tomcat_sso/"+str(PortList[3][3])+"/server.xml")
        commands.getoutput("sed -i  \'s/port=\"18030\"/port=\""+str(PortList[3][4])+"\"/g\' /apps/conf/tomcat_sso/"+str(PortList[3][3])+"/server.xml")
        commands.getoutput("sed -i  \'s/port=\"28034\"/port=\""+str(PortList[3][5])+"\"/g\' /apps/conf/tomcat_sso/"+str(PortList[3][3])+"/server.xml")
        commands.getoutput("ln -s /apps/logs/tomcat_sso/"+str(PortList[3][0])+" /apps/svr/tomcat_sso/tomcat_"+str(PortList[3][0])+"/logs")
        commands.getoutput("ln -s /apps/logs/tomcat_sso/"+str(PortList[3][3])+" /apps/svr/tomcat_sso/tomcat_"+str(PortList[3][3])+"/logs")
        commands.getoutput("rm -rf /apps/svr/tomcat_sso/apache-tomcat-7.0.70_"+str(PortList[3][0])+"/webapps")
        commands.getoutput("rm -rf /apps/svr/tomcat_sso/apache-tomcat-7.0.70_"+str(PortList[3][3])+"/webapps")
        commands.getoutput("ln -s /apps/dat/javadat/sso/service-consumer/"+str(PortList[3][0])+" /apps/svr/tomcat_sso/tomcat_"+str(PortList[3][0])+"/webapps")
        commands.getoutput("ln -s /apps/dat/javadat/sso/service-consumer/"+str(PortList[3][3])+" /apps/svr/tomcat_sso/tomcat_"+str(PortList[3][3])+"/webapps")               
        SamplePort=commands.getoutput("cat /apps/sh/sso-tomcat.sh |grep runport=")
        Ports = str(PortList[3][0])+" "+str(PortList[3][3])
        ReplacePort = "sed -i  \"s/"+SamplePort+"/runport=("+Ports+")/g\" /apps/sh/sso-tomcat.sh"
        commands.getoutput(ReplacePort)
    else:
        print Tips.ParameterError
        time.sleep(10)
        exit()
