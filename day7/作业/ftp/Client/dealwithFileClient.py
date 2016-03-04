#!/usr/bin/env python
#-*-coding:utf-8-*-

import os,json
from file_md5 import *
import dealwithFileClient
def uploadClient(sk):
    '''上传文件方法，支持批处理'''
    #filedirstr = raw_input('请输入您要上传的文件路径,若要上传多个文件，请用逗号将文件地址隔开：')
    #filedirList = filedirstr.split('filedirstr')
    filedirList = ['E:/PythonL/12-13/socket_func/socket_demo.py','D:/clientFtp/Calculator.py']
    mes = {'request':'upload','fileCount':len(filedirList)}
    jmes = json.dumps(mes)
    sk.sendall(bytes(jmes,"utf8"))
    sk.recv(1024)
    uploadChoosedir(sk)
    for filedir in filedirList:
        #filedir = 'E:\\PythonL\\12-13\\homework\\clientPac\\test.py'
        result = GetFileMd5(filedir)
        file_size = os.path.getsize(filedir)
        file_name = os.path.basename(filedir)
        if result['flag']:
            Clientmessage = {'strmd5':result['strmd5'],'fileSize':file_size,'fileName':file_name}
            jClientmessage = json.dumps(Clientmessage)
            print('jClientmessage:',jClientmessage)
            sk.sendall(jClientmessage)
            re = sk.recv(1024)
            if re:
                print(re)
                f= file(filedir,'rb')
                Flag = True
                send_size = 0
                while Flag:
                    if send_size + 1024 >file_size:
                        data = f.read(file_size-send_size)
                        Flag = False
                    else:
                        data = f.read(1024)
                        send_size+=1024
                    sk.send(data)
                f.close()
            re = sk.recv(1024)
            print('%s 上传成功!'%file_name)

def downloadClient(skd):
    '''下载文件方法，支持批处理'''
    Clientmessage = {'request':'download'}
    jClientmessage = json.dumps(Clientmessage)
    skd.sendall(jClientmessage)
    fileNumLst = dealwithFileClient.downloadChooseFile(skd)
    for fileNum in fileNumLst:
        jserverMessage = skd.recv(1024)
        serverMessage = json.loads(jserverMessage)
        recv_size = 0
        #base_path = raw_input('请输入您要下载至本地的目录：')
        base_path = 'D:/clientFtp/'
        file_dir = os.path.join(base_path,serverMessage['fileName'])
        f = file(file_dir,'wb')
        Flag = True
        print('文件正在传输，文件大小%s'%int(serverMessage['fileSize']))
        while Flag:
            if int(serverMessage['fileSize']) > recv_size:
                data = skd.recv(1024)
                recv_size += len(data)
                f.write(data)
            else:
                recv_size = 0
                Flag = False
        f.close()

        #md5验证
        result = GetFileMd5(os.path.join(base_path,serverMessage['fileName']))
        if result['flag']:
            if serverMessage['strmd5'] == result['strmd5']:
                print('下载成功！')
                skd.sendall('received')

def exitFunc(ske):
    '''与服务端建立连接'''
    Clientmessage = {'request':'exit'}
    jClientmessage = json.dumps(Clientmessage)
    ske.sendall(jClientmessage)

def printdirfile(dirDic,if_file):
    '''将服务端给的当前路径下的文件和文件夹打印出来'''
    i = 0
    if dirDic['dir']:
        print('dir : ')
        for i in range(len(dirDic['dir'])):
            print(i+1,dirDic['dir'][i])
    else:
        print('当前目录下已没有文件夹')
    if if_file:
        if dirDic['file']:
            print('file : ')
            for i in range(len(dirDic['file'])):
                print(i+1,dirDic['file'][i])
        else:
            print("当前目录下已没有文件")

def downloadChooseFile(sku):
    '''与服务端进行交互最终实现自由选择有权限的文件夹，选择该位置下的文件进行下载'''
    flag = True
    print('欢迎您使用文件上传功能，下面将进入您有权限的根目录，您可以选定直接对文件进行操作，也可以选定文件夹进入下一级菜单。')
    while flag:
        jdirDic = sku.recv(1024)
        if jdirDic != '权限不足，您不能返回上一级菜单':
            dirDic = json.loads(str(jdirDic))
        else:
            print('权限不足，您不能返回上一级菜单')
        printdirfile(dirDic,1)
        while True:
            file_or_dir = input('请输入您要选择内容。1.文件  2.文件夹  3.返回上一级：')
            if file_or_dir in ['1','2','3']:
                if file_or_dir == '1':
                    fileNum = input('请输入您要选择的文件序号,如果您要下载多个文件，请将序号按照逗号（,）隔开：')
                    fileNumLst = fileNum.split(',')
                    print(fileNumLst)
                    fileNumLstNew = map(lambda fileNum:dirDic['file'][int(fileNum)-1],fileNumLst)

                    print(fileNumLstNew)
                    mes = (1,fileNumLstNew)
                    fileNumLstNew = fileNumLstNew
                    flag = False
                elif file_or_dir == '2':
                    dirNum = input('请输入您要选择的文件夹序号：')
                    mes = (2,dirDic['dir'][int(dirNum)-1])
                elif file_or_dir == '3':
                    mes = (3,0)
                jmes = json.dumps(mes)
                sku.sendall(jmes)
                break
    return fileNumLstNew

def uploadChoosedir(skd):
    '''与服务端进行交互最终实现自由选择有权限的文件夹，选择该位置进行上传'''
    flag = True
    print('欢迎您使用文件下载功能，下面将进入您有权限的根目录，您可以选定文件夹，作为要上传的位置，或者进入下一级菜单。')
    while flag:
        jdirDic = skd.recv(1024)
        if jdirDic != '权限不足，您不能返回上一级菜单':
            dirDic = json.loads(str(jdirDic))
        else:
            print('权限不足，您不能返回上一级菜单')
        printdirfile(dirDic,0)
        while True:
            file_or_dir = input('请输入您要做的操作。0.当前文件夹 1.选定文件夹  2.进入下一级  3.返回上一级：')
            if file_or_dir in ['0','1','2','3']:
                if file_or_dir == '0':
                    mes = (0,0)
                    flag = False
                elif file_or_dir == '1':
                    fileNum = input('请输入您要选择的文件夹序号：')
                    mes = (1,dirDic['dir'][int(fileNum)-1])
                    flag = False
                elif file_or_dir == '2':
                    dirNum = input('请输入您要选择的文件夹序号：')
                    mes = (1,dirDic['dir'][int(dirNum)-1])
                elif file_or_dir == '3':
                    mes = (3,0)
                jmes = json.dumps(mes)
                skd.sendall(jmes)
                break
