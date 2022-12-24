import os
import argparse

def parsing():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', dest='file', help='Ports you want to decode')
   
    values = parser.parse_args()

    if not values.file:
        parser.error("[-] Please, give a valid argument")
    
    return values.file

def getting_output(file):

    output = os.popen("cat " + file + " | awk '{print $2}' | awk '{print $2}' FS=':' | sort -u")
    output_list = output.readlines()
    output.close()
    return output_list

def undecoding(list):
    
    for element in list:
        port = int(element, 16)
        print(port)

index = parsing()

un_ports = getting_output(index)
for i in range(len(un_ports)):
    un_ports[i] = un_ports[i].strip()

undecoding(un_ports)
