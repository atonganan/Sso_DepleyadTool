#/bin/python
import commands,Tips
def InstallNodejs():
    SelectNodejsVer = input(Tips.SelectNodejsVerTips)
    if SelectNodejsVer == 1:
        commands.getoutput("yum install -y wget")
        commands.getoutput("wget https://nodejs.org/dist/v5.6.0/node-v5.6.0-linux-x64.tar.xz")
        commands.getoutput("mkdir -p /apps/svr/nodejs")
        commands.getoutput("mv node-v5.6.0-linux-x64/* /apps/svr/nodejs/")
        commands.getoutput("echo \"export PATH=/apps/svr/nodejs/bin:$PATH\" >>/home/apps/.bashrc")
        commands.getoutput("echo \"export PATH=/apps/svr/nodejs/bin:$PATH\" >>/root/.bashrc")
    if SelectNodejsVer == 2:
        commands.getoutput("yum install -y wget")
        commands.getoutput("wget https://nodejs.org/dist/v4.5.0/node-v4.5.0-linux-x64.tar.xz")
        commands.getoutput("mkdir -p /apps/svr/nodejs")
        commands.getoutput("mv node-v4.5.0-linux-x64/* /apps/svr/nodejs/")
        commands.getoutput("echo \"export PATH=/apps/svr/nodejs/bin:$PATH\" >>/home/apps/.bashrc")
        commands.getoutput("echo \"export PATH=/apps/svr/nodejs/bin:$PATH\" >>/root/.bashrc")