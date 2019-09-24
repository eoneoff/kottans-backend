#!/usr/bin/env python


import socket
import sys
import re

def parseArguments(args):
    host = ""
    ports = range(1,65536)
    if '--host' not in args or args.index('--host') == len(args)- 1:
        raise ValueError("You must specify a host to scan ports")
    else:
        host = args[args.index('--host') + 1]
        if not re.search('^((25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(25[0-5]|2[0-4]\d|[01]?\d?\d)$', host):
            raise ValueError("You must specify a valid host IP address")
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
    pass

if __name__ == "__main__":
    try:
        scan(*parseArguments(sys.argv[1:]))
    except ValueError as er:
        print(er)
            

