import os    
import ftplib
import zlib
import time
import paramiko
import socket
import serial
import fnmatch
import re
import json

command_slot0 = r""
command_slot1 = r""
command_slot2 = r""
description_to_save_test = r"Sw Save test "
description_to_activate_test = r"Sw Activate test "
description_slot0 = r""
description_slot1 = r""
description_slot2 = r""
json_nesting_0 = r""
json_nesting_1 = r""
tuple_position0 = 0
list_position0 = 0
save_activate_status_ok = u""

class Swup_regression():

        def __init__(self,file_path, host_name, password):
            self.file_path = file_path
            self.host_name = host_name
            self.password = password
            self.tel_port = 22
            self.save_prefix = r""
            self.activate_prefix = r""
            self.inventory_command = r""
            self.path = r""
            self.double_slash = r"\\"
            self.raport_path = self.path + "raport\\"

        def file_name(self):
            for files in os.listdir(self.file_path):
                return str(os.path.basename(files))
        
        def calculatechecksum(self):
            try:
                for file_name in os.listdir(self.file_path):
                    with open(self.file_path + file_name, "rb") as files:
                        data = files.read()
                        checksum = hex((zlib.adler32(data) & 0xffffffff))
                        checksum = checksum.rstrip("L")
                        return checksum
            except Exception, e:
                    print str(e)

        def download(self):
            for file_name in os.listdir(self.file_path):
                ftp = ftplib.FTP(self.host_name, self.password,"")
                with open(self.file_path + file_name, "rb") as files:
                    ftp.storbinary("STOR " + file_name, files)
                    ftp.quit()
                print  ("File " + os.path.basename(file_name) + " sent to Device") 
                return os.path.basename(file_name)

        def check_download(self):
            ftp = ftplib.FTP(self.host_name, self.password,"")
            for file_name in os.listdir(self.file_path):
                if file_name in ftp.nlst():
                    self.test_passed(r"download")
                else:
                    self.test_not_passed(r"download")
            ftp.quit()
            ftp.close()        
        
        def test_passed(self, test_name):
            print test_name + " passed"
            with open(self.raport_path + "raport.txt", "a") as files:
                files.write(test_name + " passed\n")

        def test_not_passed(self, test_name):
            print test_name + " not passed"
            with open(self.raport_path +  "raport.txt", "a") as files:
                files.write(test_name + " not passed\n")
        
        def command_to_save(self):
             save_command = str(self.save_prefix + self.file_name() + " "+ 
             self.calculatechecksum()+ " "  +
              self.file_name().strip("")+ ""+ " "+ 
              (self.file_name()).strip("")+ "")
             return save_command
        
        def command_to_activate(self):
            activate_command = str(self.activate_prefix +  
            " "+ str(self.file_name()).strip(""))+ 
            "" + " "  + str(self.file_name()).strip("")+ 
            ""+ " " + self.file_name()+ " "  + self.file_name().strip("")
             + ""
            return activate_command

        def send_command(self,command, description):
            try:
                print description + self.file_name()
                client = paramiko.SSHClient() 
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                sock = socket.socket()
                sock.connect((self.host_name, self.tel_port))
                t = paramiko.Transport(sock)
                t.connect()
                t.auth_none("root")
                client._transport = t  
                stdin, stdout, stderr=client.exec_command(command)   
                output1 = "".join(stdout.readlines())
                output_err1=  "".join(stderr.readlines())         
                output1.split(",")
                output_err1.split(",") 
                print output1.split(",")                       
                return output1, output_err1                                 
            except Exception, e:
                print str(e)
        
        def checks_slot(self,command, description):
            try:
                print description
                client = paramiko.SSHClient() 
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                sock = socket.socket()
                sock.connect((self.host_name, self.tel_port))
                t = paramiko.Transport(sock)
                t.connect()
                t.auth_none("root")
                client._transport = t  
                stdin, stdout, stderr=client.exec_command(command)   
                output1 = "".join(stdout.readlines())
                output_err1=  "".join(stderr.readlines()) 
                n = json.loads((output1))
                print n["value0"]["value4"]                         
                return n, output1                                 
            except Exception, e:
                print str(e)

        def software_save_activate(self, command, description):
            try:
                print description + self.file_name()
                client = paramiko.SSHClient() 
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                sock = socket.socket()
                sock.connect((self.host_name, self.tel_port))
                t = paramiko.Transport(sock)
                t.connect()
                t.auth_none("root")
                client._transport = t    
                stdin, stdout, stderr=client.exec_command(command) 
                output1 = "".join(stdout.readlines())
                output_err1=  "".join(stderr.readlines())        
                output1.split(",")
                output_err1.split(",")                          
                return output1, output_err1          
            except Exception, e:
                print str(e)

        def parser_if_list_output(self, function, position, element, function_to_check_name):
                if  element in function[position]:
                    self.test_passed(function_to_check_name)
                else: 
                    self.test_not_passed(function_to_check_name)
        
        def parser_if_json_output(self, function, tuple_position, function_to_check_name, json_nesting_0, json_nesting_1, value):
                if function[tuple_position][json_nesting_0][json_nesting_1] == value:
                    self.test_passed(function_to_check_name)
                else:
                    self.test_not_passed(function_to_check_name)
                
a = Swup_regression(r"", r"***.***.***.*", r"root")




    
