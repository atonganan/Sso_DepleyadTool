#coding:gb2312
#!/usr/bin/python
import Deployed_Java,Deployed_Sso_Tomcat,Deployed_Fastdfs_Java,Configure_nginx
import Deployed_Fastdfs_Tomcat,Initialize,LastAction,Tips,Check,InstallNodejs
print Tips.WelcomeInfo
print Tips.ServiceInfo
Check.CheckRunPath()
MenuSelect = input(Tips.MenuSelectTips)
if MenuSelect == 1:
    Initialize.Initalize()
    Deployed_Java.Deployed_java()
    LastAction.ChangeApps()
elif MenuSelect == 2:
    Initialize.Initalize()
    Deployed_Sso_Tomcat.Deployed_Sso_Tomcat()
    LastAction.ChangeApps()
elif MenuSelect == 3:
    Initialize.Initalize()
    Deployed_Fastdfs_Java.Deployed_Fastdfs_Tomcat()
    LastAction.ChangeApps()
elif MenuSelect == 4:
    Initialize.Initalize()
    Deployed_Fastdfs_Tomcat.Deployed_Fastdfs_Tomcat()
    LastAction.ChangeApps()
elif MenuSelect == 5:
    Configure_nginx.ConfigureNginx()
    LastAction.ChangeApps()
elif MenuSelect ==6:
    InstallNodejs.InstallNodejs()
    LastAction.ChangeApps()
elif MenuSelect == 7:
    Initialize.Initalize()
    Deployed_Java.Deployed_java()
    Deployed_Sso_Tomcat.Deployed_Sso_Tomcat()
    Deployed_Fastdfs_Java.Deployed_Fastdfs_Tomcat()
    Deployed_Fastdfs_Tomcat.Deployed_Fastdfs_Tomcat()
    LastAction.ChangeApps()
    
elif MenuSelect == 8:
    exit()
else:
    exit()