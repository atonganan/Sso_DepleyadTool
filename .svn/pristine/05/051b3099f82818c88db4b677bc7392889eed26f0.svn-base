import time,commands,PortCheck
def GetTime():
    NowDate = time.strftime('%Y%m%d',time.localtime(time.time()))
    return NowDate
def GetHostName():
    hostname = commands.getoutput("hostname")
    return hostname
def GetPortList():
    PortList = PortCheck.PortSelect(GetHostName())
    return PortList