#!/usr/bin/env python
"""Simplle port sniffer

This is a simple port sniffer, which can be calles as command line script or imported as a module.
When used from command line it takes 2 named paramentes:
--host      obligatory parameter which defines the host address for a port scan.
            After the --host parameter should follow the host IP addres as four numbers,
            separated by commas or a host web address.

                python sniffer.py --host www.google.com

--ports     optional parementer to provide a port range for scan. The range
            should be definded as two number with a dash between them. If not set
            or set incorrectly the default range of (1-65535) is scanned

                python sniffer.py --host wwww.google.com --ports 1024-2018

--help      parameted to see this reference

To import port scanner use

    import sniffer.py

after import you can perform scan by calling sniffer.scan()

scan(host, portString, module, silent)

For  detailed disambiguation of scan function use help(scan) after importing
sniffer or call sniffer.py with --help method
"""


import socket
import sys
import re

def _twister():
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

def _parseHost(host):
    if not re.search('^((25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(25[0-5]|2[0-4]\d|[01]?\d?\d)$', host):
        try:
            return socket.gethostbyname(host)
        except socket.gaierror as er:
            er.args="Hostname could not be resolved"
            raise er
    else: return host

def _parsePorts(ports):
    if not re.search('^\d{1,4}-\d{1,4}$', ports):
        raise ValueError
    limits = [int(i) for i in ports.split('-')]
    if limits[0] >= limits[1] or any([i not in range(1, 65536) for i in limits]):
        raise ValueError
    else:
        return range(limits[0], limits[1]+1)


def _parseArguments(args):
    host = ""
    ports = range(1,65536)
    if '--host' not in args or args.index('--host') == len(args)- 1:
        raise ValueError("You must specify a host to scan ports")
    else:
        host = _parseHost(args[args.index('--host') + 1])        
    if '--ports' in args:
        index = args.index('--ports') + 1
        if index == len(args):
            print("Invalid ports specified, setting to default (1-65535)")
        else:
            try:
                ports = _parsePorts(args[index])
            except ValueError:
                print("Invalid ports specified, setting to default (1-65535)")
    return(host, ports)

def _scan(host, ports, module = False, silent = False):
    socket.setdefaulttimeout(0.3)
    openPorts=[]
    tw = _twister()
    print('scanning', end = ' ', flush=True)
    for port in ports:
        with socket.socket() as s:
            if s.connect_ex((host, port)) == 0:
                openPorts.append(port)
                print('.', end=' ', flush=True)
            else:
                print(f'{next(tw)}\b',end='',flush=True)
    if not silent or not module:
        result = ''
        if len(openPorts):
            result = "Port{} {} {}".format('s' if len(openPorts)%1 == 1 else '',
            ' '.join((str(p) for p in openPorts)), "are" if len(openPorts) > 1 else "is")
        else:
            result = "No ports are"
        print(f' \n{result} open')
    if module: return openPorts

    

def scan(host, portsString = '', module = True, silent = False):
    """Simple port scanning method

    This is a method for port scanning. It takes one oblicatory argument 'host' and three
    optional arguments 'portString', 'module' and 'silent'

    host:str        an obligatory argument, which provies a host for scanning. It can be an
                    IP address as string of four numbers, separated by dots or a hostname

    posrtString:str an optional argument to define a range of scanned ports. Should be provideed
                    as a string, composed of two numbers, separated by dash. If not provided or
                    provided incorrectly the port range will be set to default full range (1-65535)

    module:bool     a bool argument, which tells the function to run as a module, that is to
                    return a result as a list of open ports

    silent:bool     a bool argument, which tells the function to supress the output and run
                    and run in silent mode. Takes effect only if 'modlue' parameter is also
                    set to 'True'
    """
    try:
        host = _parseHost(host)
    except Exception as er:
        print(er)
        print(__doc__)
        return
    ports = range(1, 65536)
    if portsString:
        try:
            ports = _parsePorts(portsString)
        except:
            print ("Invalid ports specified, setting to default (1-65535)")
    return _scan(host, ports, module, silent)

        




if __name__ == "__main__":
    if '--help' in sys.argv:
        index = sys.argv.index('--help') + 1
        if index != len(sys.argv) and sys.argv[index] == 'method': help(scan)
        else: print(__doc__)
    else:
        try:
            _scan(*_parseArguments(sys.argv[1:]))
        except Exception as er:
            print(f'\n{er}\n')
            print(__doc__)
            

