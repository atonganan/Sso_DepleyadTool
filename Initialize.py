import commands,time,Tips
def Initalize():
    print Tips.NowServer
    time.sleep(10)
    FileCheck = commands.getoutput("cd /tmp/ && ls | grep apps*.tar.gz")
    commands.getoutput("rm -rf /tmp/apps ")
    commands.getoutput("cd /tmp/ && tar zxvf "+FileCheck)
    commands.getoutput("mkdir /tmp/Deplaytmp")
    commands.getoutput("mv /tmp/apps/zabbix /tmp/Deplaytmp/")
    commands.getoutput("mv /tmp/apps /apps")
    commands.getoutput("chown -R apps.apps /apps")
    WriteDns = str('echo "10.0.0.86 TEST_MYSQL_MASTER" >>/etc/hosts && echo "10.0.0.86 TEST_MYSQL_READ" >>/etc/hosts')
    commands.getoutput(WriteDns)
