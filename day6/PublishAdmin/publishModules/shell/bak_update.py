#!/usr/bin/python
# -*- coding: utf-8 -*-
#########################
#   Auther:zhanghao     #
#########################

#####本更新程序包括3个文件 
#####update.py 更新脚本 
#####mod.ini 更新服务器及模块 等配置信息
#####exclude.txt 同步时需要排除的文件 一行一个文件名称

#####配置文件中如果是jar包 mod_name必须和jar包名一样
#####本地文件夹名称必须和模块名称一样，可以是文件夹也可以是tar.gz或者zip包


import sys,os,pexpect,fileinput,paramiko,datetime,time
from ConfigParser import ConfigParser
##########变量设置#################
#开始时间（结束后有个结束时间，两者相减即程序运行时间）
starttime=datetime.datetime.now()
#today="2014-5-21-101110"
today=time.strftime("%Y-%-m-%-d-%-H%-M%-S",time.localtime())
#根目录
base_dir = "/var/www/html/" #"/home/kingkong/www/php/" #/www/
#程序上传目录
#src_dir="/home/zhanghao/文档/"+ today
src_dir=base_dir+"PublishAdmin/publishModules/upload"
#本地主机同步目录
dst_dir=base_dir+"PublishAdmin/publishModules/upload/"+ today
#模块信息配置文件
mod_file=base_dir+"PublishAdmin/publishModules/shell/mod.ini"
#同步需要排除的文件
exclude_file=base_dir+"PublishAdmin/publishModules/shell/exclude.txt"
#配置文件多IP分隔符
s_field='|'

#读取配置文件
#模块IP/路径/模块类型
#PS:如果有tomcat 还需指定tomcat路径（重启tomcat服务用）
cf=ConfigParser()
cf.read(mod_file)


def helpFunc(a,b,c,d):
    print ""
    print "usage: update.py -m module_name -a action_type"
    print "-l will only print all of the mod_name and exit"
    print "module_name provide module_name to update"
    print ""
    print "action type is update|backup|rollback|full_update|test_update"
    print ""
    print "list mod:"
    print cf.sections()
    sys.exit(3)

def verFunc(a,b,c,d):
    print "Ver 0.0.1"
    sys.exit(3)



from optparse import OptionParser
parser = OptionParser(add_help_option=0)
parser.add_option("-h", "--help", action="callback", callback=helpFunc)
parser.add_option("-V", "--version", action="callback", callback=verFunc)
parser.add_option("-m", "--module", action="store", type="string",dest="mod",default="")
parser.add_option("-a", "--action", action="store", type="string",dest="act",default="")
parser.add_option("-l", "--list", action="store_true", dest="list")

(options, args) = parser.parse_args()
mod_name=options.mod
action=options.act

#如果指定-l，仅列出模块列表 安全退出
if options.list:
    print cf.sections()
    sys.exit(0)


#如果没有指定模块名或者动作,打印错误并退出 
if mod_name or action:
    pass
else:
    print '''you don't have mod_name and action!\nuse -h get some help'''
    sys.exit()

#如果模块不在模块列表中，打印错误信息并退出
if not cf.has_section(mod_name):
    sys.exit("mod_name %s not in mod_list\nmod_list must in \n %s \n\n see %s get more information" % (mod_name,cf.sections(),mod_file))

#在远程主机上执行命令的函数
def run_command(cmd):
    print cmd
    client=paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(hostname=host, port=port,username=user,password=password)
    stdin,stdout,stderr = client.exec_command(cmd)
    print stderr.read()
    print stdout.read()
    client.close()


class haixuan:

    def __init__(self,mod_name='',host='',port='',src_file='',dst_file='',user='',password='',is_compress=''):
        self.mod_name = mod_name
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.is_compress = is_compress
        self.src_file = src_file
        self.dst_file = dst_file

    def prepare_file(self):
        #查看是否有该模块的打包文件
        #判断是否有压缩包
        #if cf.has_option(mod_name,'is_compress') and cf.get(mod_name,'is_compress') == 'True':
        if is_compress == 'True':
            if os.path.exists("%s" % src_file+".tar.gz") or os.path.exists("%s" % src_file+".zip") or os.path.exists("%s" % dst_file+".tar.gz") or os.path.exists("%s" % dst_file+".zip"):
        #如果是压缩包先解压
        #复制文件到本地同步目录
                if type == "java":
                    os.path.exists(dst_dir) or os.makedirs(dst_dir)
                    os.chdir(dst_dir)
                    os.system("cp %s.tar.gz %s 2>/dev/null||cp %s.zip %s 2>/dev/null " % (src_file,dst_dir,src_file,dst_dir))
                elif type == "c" or type == "php":
                    os.path.exists(dst_file) or os.makedirs(dst_file)
                    os.chdir(dst_file)
                    os.system("cp %s.tar.gz %s 2>/dev/null||cp %s.zip %s 2>/dev/null " % (src_file,dst_file,src_file,dst_file))
                else:
                    print "mod_type error"
                    sys.exit()
                #print os.path.abspath(os.path.curdir)
                os.system("tar xzf %s.tar.gz 2> /dev/null||unzip %s.zip >/dev/null 2>&1" % (mod_name,mod_name))
                #print "tar xzf %s.tar.gz 2> /dev/null||unzip %s.zip 2>/dev/null" % (mod_name,mod_name)
                os.system("rm -f %s.tar.gz 2>/dev/null;rm -f %s.zip >/dev/null 2>&1" % (mod_name,mod_name))
                #print "rm -f %s.tar.gz 2>/dev/null;rm -f %s.zip 2>/dev/null" % (mod_name,mod_name)
                if type == "c":
                    os.system("[ -d %s ] && mv %s/* ./ && rmdir %s" % (mod_name,mod_name,mod_name))
        else:
            #如果没有压缩包 是否有文件夹
            if os.path.exists("%s" % src_file):
                os.system(cp -a %s %s) % (src_file,dst_file)
            #如果都没有 退出
            else:
                print src_dir + " does't have " + mod_name + " directory"
                sys.exit()



    def stop_program(self):
        #关闭应用
        if type == "java":
            self.webapp=cf.get(mod_name,"tomcat_path")
            rcmd='''ps aux|grep %s|grep -v grep|awk '{print $2}'|xargs kill -9;rm -rf %s/work/Catalina/''' % (self.webapp,self.webapp)
            run_command(rcmd)
        elif type == "jar":
            rcmd='''ps aux|grep %s|grep -v grep|awk '{print $2}'|xargs kill -9''' % (mod_name)
            run_command(rcmd)
        elif type == "c":
            self.pname=remote_dst_file.split("/")[-1]
            rcmd='''bash -c "ps -ef|grep -i %s|grep -v grep|awk '{print $2}'|xargs kill -9"'''  % self.pname
            run_command(rcmd)
        else:
            pass

    def start_program(self):
        #启动应用
        if type == "java":
            rcmd='source /etc/profile && %s/bin/startup.sh' % self.webapp
            run_command(rcmd)
        elif type == "c":
            #rcmd='''cd %s && ./bin/* &''' % remote_dst_file
            rcmd='''cd %s &&  find ./bin  -path "*bak" -prune -o  -type f -exec test -x {} \; -a -exec ls {} \;|xargs -I a nohup a''' % remote_dst_file
            run_command(rcmd)
        elif type == "jar":
            rcmd='''cd %s && nohup java -jar `ls -rt *.jar|tail -1` &''' % remote_dst_file
            run_command(rcmd)
        else:
            pass


    def update(self):
        #同步更新到远程服务器
        self.prepare_file()
        self.stop_program()
        rcmd="rsync -e 'ssh -p %s' -avz --exclude-from=%s %s %s@%s:%s" % (port,exclude_file,dst_file+"/",user,host,remote_dst_file+"/")
        print rcmd
        outfile=pexpect.run (rcmd, events={'(?i)password': password+'\n','continue connecting (yes/no)?':'yes\n'},timeout=None)
        print outfile
        print ""
        self.start_program()

    def backup(self):
        #备份操作
        print "backup start"
        os.path.exists(local_backup_dir) or os.makedirs(local_backup_dir)
        backup_cmd="scp -P %s -r %s@%s:%s %s" % (port,user,host,remote_dst_file,local_backup_dir)
        print backup_cmd
        outfile=pexpect.run (backup_cmd, events={'(?i)password': password+'\n','continue connecting (yes/no)?':'yes\n'},timeout=None)
        print outfile
        print ""
        print "%s backup successful!" % mod_name

    def rollback(self):
        #回滚
        rcmd="rsync -e 'ssh -p %s' -avz --delete --exclude-from=%s %s %s@%s:%s" % (port,exclude_file,local_backup_dir+"/"+mod_name+"/",user,host,remote_dst_file+"/")
        print rcmd
        outfile=pexpect.run (rcmd, events={'(?i)password': password+'\n','continue connecting (yes/no)?':'yes\n'},timeout=None)
        print outfile
        print ""

    def full_update(self):
        #全量更新
        self.prepare_file()
        self.stop_program()
        self.exclude_file=""
        rcmd="rsync -e 'ssh -p %s' -avz --exclude-from=%s %s %s@%s:%s" % (port,self.exclude_file,dst_file+"/",user,host,remote_dst_file+"/")
        print rcmd
        outfile=pexpect.run (rcmd, events={'(?i)password': password+'\n','continue connecting (yes/no)?':'yes\n'},timeout=None)
        print outfile
        print ""
        self.start_program()


    def test_update(self):
        self.prepare_file()
        rcmd="rsync -e 'ssh -p %s' -avz -n --exclude-from=%s %s %s@%s:%s" % (port,exclude_file,dst_file+"/",user,host,remote_dst_file+"/")
        print rcmd
        outfile=pexpect.run (rcmd, events={'(?i)password': password+'\n','continue connecting (yes/no)?':'yes\n'},timeout=None)
        print outfile
        print ""



host_list=cf.get(mod_name,'ip').split(s_field)
for host in host_list:
    #获取给定模块的主机IP、路径和程序类型
    #获取文件路径和cp路径必须获取模块名后才能确定 所以没写在上面的变量设定中
    #print host
    host_index=host_list.index(host)
    try:
        remote_dst_file=cf.get(mod_name,"path")
        type=cf.get(mod_name,"type")
        #如果有端口/用户/密码选项则读取，没有则默认为37815/root/123456
        #如果有多个IP/端口/用户/密码 则根据list中的index查找
        if cf.has_option(mod_name,'user') and len(host_list)>host_index:
            user_list=cf.get(mod_name,'user').split(s_field)
            user=user_list[host_index]
        elif cf.has_option(mod_name,'user'):
            user=cf.get(mod_name,'user')
        else:
            user='root'
        if cf.has_option(mod_name,'password') and len(host_list)>host_index:
            password_list=cf.get(mod_name,'password').split(s_field)
            password=password_list[host_index]
        elif cf.has_option(mod_name,'password'):
            password=cf.get(mod_name,'password')
        else:
            password='123456'
        if cf.has_option(mod_name,'port') and len(host_list)>host_index:
            port_list=cf.get(mod_name,'port').split(s_field)
            port=port_list[host_index]
        elif cf.has_option(mod_name,'port'):
            port=cf.get(mod_name,'port')
        else:
            port=37815
        #判断上传文件是否是压缩包
        if cf.has_option(mod_name,'is_compress') and cf.get(mod_name,'is_compress') == 'True':
            is_compress='True'
        else:
            is_compress='False'
        #上传文件夹名称
        src_file=src_dir + "/" + mod_name
        #dst_file=dst_dir + "/" + mod_name
        #同步文件夹名称
        dst_file=dst_dir + "/"
        #本地备份文件夹名称
        local_backup_dir=dst_dir + "/backup"
        #print local_backup_dir,src_file,dst_file
        #print user,password,port
    except Exception as e:
        print e
        sys.exit("mod_name error!")

    t=haixuan(mod_name=mod_name,host=host,port=port,src_file=src_file,dst_file=dst_file,user=user,password=password,is_compress=is_compress)
    try:
        eval("t.%s()" % action)
    except Exception as e:
        print e
        print '''this instance doesn't have this method name'''



endtime=datetime.datetime.now()
print "this program consumed %s seconds " % (endtime - starttime)
