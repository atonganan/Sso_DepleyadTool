import commands,GetInfo
def ConfigureNginx():
    PortList = GetInfo.GetPortList() 
    commands.getoutput("mkdir -p /tmp/NginxConfBak/"+GetInfo.GetTime()+" && mv /apps/conf/nginx/* /tmp/NginxConfBak/"+GetInfo.GetTime()+"/")
    commands.getoutput("mkdir -p /apps/logs/nginx && ln -s /apps/logs/nginx /apps/svr/nginx/logs && rm -rf /apps/svr/nginx/logs/nginx")
    commands.getoutput("cd /root/Sso_DeployedTools/ext/ && tar xvf nginx.tar && cp -R /root/Sso_DeployedTools/ext/nginx/* /apps/conf/nginx/")
    commands.getoutput("sed -i  \'s/8204/"+str(PortList[3][0])+"/g\' /apps/svr/nginx/conf/nginx.conf")
    commands.getoutput("sed -i  \'s/8205/"+str(PortList[3][3])+"/g\' /apps/svr/nginx/conf/nginx.conf")
    commands.getoutput("sed -i  \'s/9202/"+str(PortList[1][0])+"/g\' /apps/svr/nginx/conf/nginx.conf")