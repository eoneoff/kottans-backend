#!/usr/bin/env python


import socket
import sys
import re

def twister():
    current = '\\'
    while True:
        if current == '\\':
            current = '|'
            yield current
        elif current == '|':
            current = '/'
            yield current
        elif current == '/':
            current = '-'
            yield current
        else:
            current = "\\"
            yield current

def parseArguments(args):
    host = ""
    ports = range(1,65536)
    if '--host' not in args or args.index('--host') == len(args)- 1:
        raise ValueError("You must specify a host to scan ports")
    else:
        host = args[args.index('--host') + 1]
        if not re.search('^((25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(25[0-5]|2[0-4]\d|[01]?\d?\d)$', host):
            try:
               host = socket.gethostbyname(host);
            except socket.gaierror as er:
                er.args="Hostname could not be resolved"
                raise er
    if '--ports' in args:
        index = args.index('--ports') + 1
        if index == len(args) or not re.search('^\d{1,4}-\d{1,4}$', args[index]):
            print("Invalid ports specified, setting to default (1-65535)")
        else:
            limits = [int(i) for i in args[index].split('-')]
            if limits[0] >= limits[1] or any([i not in range(1, 65536) for i in limits]):
                print("Invalid ports specified, setting to default (1-65535)")
            else:
                ports = range(limits[0], limits[1]+1)
    return(host, ports)

def scan(host, ports):
    socket.setdefaulttimeout(0.3)
    openPorts=[]
    tw = twister()
    print('scanning', end = ' ', flush=True)
    for port in ports:
        with socket.socket() as s:
            if s.connect_ex((host, port)) == 0:
                openPorts.append(port)
                print('.', end=' ', flush=True)
            else:
                print(f'{next(tw)}\b',end='',flush=True)
    result = ''
    if len(openPorts):
        result = "Port{} {} {}".format('s' if len(openPorts)%1 == 1 else '',
        ' '.join((str(p) for p in openPorts)), "are" if len(openPorts) > 1 else "is")
    else:
        result = "No ports are"
    print(f' \n{result} open')



if __name__ == "__main__":
    try:
        scan(*parseArguments(sys.argv[1:]))
    except Exception as er:
        print(er)
            

