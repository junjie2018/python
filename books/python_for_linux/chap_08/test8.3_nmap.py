import nmap

nm = nmap.PortScanner()
nm.scan('www.baidu.com', '22-1000')
print(nm.command_line())
print(nm.scaninfo())
print(nm.all_hosts())
print(nm['14.215.177.39'].state())
print(nm['14.215.177.39'].all_protocols())
print(nm['14.215.177.39']['tcp'].keys())
print(nm['14.215.177.39']['tcp'][80])

nm.scan(hosts='192.168.input.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
