#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jly'
import os,json
from userClass import *
import logging

logging.basicConfig(filename='log.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)

class dealwithServer(userServer):
    '''dealwithServer、下载。支持批量上传和下载'''
    def receiveUpload(self,strmd5,fileSize,fileName):
        '''receiveUpload,处理文件的上传，支持批处理'''
        self.conn.sendall('received')
        #base_path = 'D:/serverFtp/'
        recv_size = 0
        file_dir = os.path.join(self.currentDir,fileName)
        f = file(file_dir,'wb')
        Flag = True
        while Flag:
            if int(fileSize) > recv_size:
                data = self.conn.recv(1024)
                recv_size += len(data)
                f.write(data)
            else:
                recv_size = 0
                Flag = False
        f.close()
        #md5
        result = userServer.GetFileMd5(os.path.join(self.currentDir,fileName))
        if result['flag']:
            if strmd5 == result['strmd5']:
                print 'success'
                self.conn.sendall('上传成功！')
                logging.info('%s upload success'%fileName)

    def receiveDownlode(self):
        '''receiveUpload,处理文件的下载，支持批处理'''
        filedirLst = self.chooseDirD()
        print 'filedirLst:',filedirLst
        #filedir = 'D:/serverFtp/test.py'
        for filedir in filedirLst:
            result = userServer.GetFileMd5(filedir)
            file_size = os.path.getsize(filedir)
            file_name = os.path.basename(filedir)
            if result['flag']:
                Clientmessage = {'strmd5':result['strmd5'],'fileSize':file_size,'fileName':file_name}
                jClientmessage = json.dumps(Clientmessage)
                self.conn.sendall(jClientmessage)
                receive = self.conn.recv
                if receive:
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
                        self.conn.send(data)
                    f.close()
                    result = self.conn.recv(1024)
                    print 'client download %s %s'%(file_name,result)
                    logging.info('%s download success'%file_name)