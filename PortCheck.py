#!/bin/python
import config

def PortSelect(hostname):
    if hostname == "JKM-UNCTL-074":
        FastdfsJavaPort = config.JKMUNCTL074fastdfsjava
        FastdfsTomcatPort = config.JKMUNCTL074tomcatfastdfs
        SsoJavaPort = config.JKMUNCTL074ssojava
        SsoTomcatPort = config.JKMUNCTL074tomcatsso
    elif hostname == "JKM-UNCTL-107":
        FastdfsJavaPort = config.JKMUNCTL107fastdfsjava
        FastdfsTomcatPort = config.JKMUNCTL107tomcatfastdfs
        SsoJavaPort = config.JKMUNCTL107ssojava
        SsoTomcatPort = config.JKMUNCTL107tomcatsso
    elif hostname == "JKM-UNCTL-205":
        FastdfsJavaPort = config.JKMUNCTL205fastdfsjava
        FastdfsTomcatPort = config.JKMUNCTL205tomcatfastdfs
        SsoJavaPort = config.JKMUNCTL205ssojava
        SsoTomcatPort = config.JKMUNCTL205tomcatsso
    elif hostname == "JKM-SSO-062":
        FastdfsJavaPort = config.JKMSSO062fastdfsjava
        FastdfsTomcatPort = config.JKMSSO062tomcatfastdfs
        SsoJavaPort = config.JKMSSO062ssojava
        SsoTomcatPort = config.JKMSSO062tomcatsso
    elif hostname == "JKM-SSO-068":
        FastdfsJavaPort = config.JKMSSO068fastdfsjava
        FastdfsTomcatPort = config.JKMSSO068tomcatfastdfs
        SsoJavaPort = config.JKMSSO068ssojava
        SsoTomcatPort = config.JKMSSO068tomcatsso
    elif hostname == "JKM-UNCTL-167":
        FastdfsJavaPort = config.JKMUNCTL167fastdfsjava
        FastdfsTomcatPort = config.JKMUNCTL167tomcatfastdfs
        SsoJavaPort = config.JKMUNCTL167ssojava
        SsoTomcatPort = config.JKMUNCTL167tomcatsso
    elif hostname == "JKM-UNCTL-168":
        FastdfsJavaPort = config.JKMUNCTL168fastdfsjava
        FastdfsTomcatPort = config.JKMUNCTL168tomcatfastdfs
        SsoJavaPort = config.JKMUNCTL168ssojava
        SsoTomcatPort = config.JKMUNCTL168tomcatsso
    elif hostname == "JKM-UNCTL-169":
        FastdfsJavaPort = config.JKMUNCTL169fastdfsjava
        FastdfsTomcatPort = config.JKMUNCTL169tomcatfastdfs
        SsoJavaPort = config.JKMUNCTL169ssojava
        SsoTomcatPort = config.JKMUNCTL169tomcatsso
    elif hostname == "JKM-INT-189":
        FastdfsJavaPort = config.JKMINT189fastdfsjava
        FastdfsTomcatPort = config.JKMINT189tomcatfastdfs
        SsoJavaPort = config.JKMINT189ssojava
        SsoTomcatPort = config.JKMINT189tomcatsso
    return FastdfsJavaPort,FastdfsTomcatPort,SsoJavaPort,SsoTomcatPort
