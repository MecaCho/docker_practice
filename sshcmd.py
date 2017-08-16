#-*- coding: utf-8 -*-
#!/usr/bin/python 
import paramiko
import threading

def ssh2(ip,username,passwd,cmd):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=11111111115)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
#           stdin.write("Y")   #简单交互，输入 ‘Y’ 
            out = stdout.readlines()
            #屏幕输出
            for o in out:
                print o,
        print '%s\tOK\n'%(ip)
        ssh.close()


if __name__=='__main__':
    cmd = ['systemctl stop kubelet']#你要执行的命令列表
    username = "huawei"  #用户名
    passwd = "huawei"    #密码
    threads = []   #多线程
    print "Begin......"
    ip = "162.3.210.31"
    a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
    a.start() 
