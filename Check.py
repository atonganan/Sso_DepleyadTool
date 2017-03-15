#!/bin/python
import commands,time,Tips
def CheckRunPath():
    print Tips.BeforeConfirmTips
    print Tips.ConfirmTips
    print Tips.ConfirmTips
    Confirm = raw_input(Tips.ConfirmTips)
    if Confirm == "y":
        print Tips.ConfirmLoadingTips
    elif Confirm == "Y":
        print Tips.ConfirmLoadingTips
    else:
        exit()
    RunningRole= commands.getoutput("whoami")
    if RunningRole != "root":
        print RunningRole+Tips.ChcekRoot
        time.sleep(10)
        exit()
    FileCheckCount = commands.getoutput("cd /tmp/ && ls | grep -c apps*.tar.gz")
    if FileCheckCount < "1":
        print RunningRole+Tips.FileCheckNotFound
        time.sleep(10)
        exit()
    elif FileCheckCount > "1":
        print RunningRole+Tips.FileCheckMultipleFiles
        time.sleep(10)
        exit()
    JavaProcess = commands.getoutput("ps aux |grep -c java")
    if JavaProcess > "2":
        print RunningRole+Tips.CheckTooManyJavaProcess
        time.sleep(10)
        exit()
    TomcatProcess = commands.getoutput("ps aux |grep -c tomcat")
    if TomcatProcess > "2":
        print RunningRole+Tips.CheckTooManyTomcatProcess
        time.sleep(10)
        exit()
    FastdfsProcess = commands.getoutput("ps aux |grep -c fastdfs")
    if FastdfsProcess > "2":
        print RunningRole+Tips.CheckTooManyfastdfsProcess
        time.sleep(10)
        exit()