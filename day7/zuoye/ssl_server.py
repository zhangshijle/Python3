#/usr/bin/env  python
# -*- coding:utf-8 -*-
import  os
import  socketserver
import  ssl,subprocess



class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print("sss")
        conn = self.request
        print("starting..",self.client_address)

        Flag = True
        while Flag:
            data1 = conn.recv(1024)
            if not data1:
                break
            print("recv cmd:",str(data1,'utf8'))
            cmd = str(data1,"utf8").strip()
            cmd_call = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE)
            cmd_result = cmd_call.stdout.read()
            if len(cmd_result) == 0:
               cmd_result = b"cmd execution has no output.."

            ack_msg = bytes("CMD_RESULT_SIZE|%s" %len(cmd_result) ,"utf8")

            conn.send(ack_msg)
            client_ack = conn.recv(50)
            if client_ack.decode() == 'CLIENT_READY_TO_RECV':
                conn.send(cmd_result )

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1",12345),Myserver)
    server.serve_forever()




