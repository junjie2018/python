import telnetlib


def conn_scan(host, port):
    t = telnetlib.Telnet()
    try:
        t.open(host, port, timeout=1)
        print(host, port, 'is avaliable')
    except Exception as e:
        print(host, port, 'is not avaliable')
    finally:
        t.close()


def main():
    host = 'www.baidu.com'
    for port in range(80, 5000):
        conn_scan(host, port)


if __name__ == '__main__':
    main()
