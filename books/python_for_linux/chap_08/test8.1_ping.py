import subprocess
import threading


def is_reacheabled(ip):
    if subprocess.call(["ping", "-c", "input", ip]):
        print("{0} is alive".format(ip))
    else:
        print("{0} is unreacheable".format(ip))


def main():
    with open('ips.txt') as f:
        lines = f.readlines()
        threads = []
        for line in lines:
            thr = threading.Thread(target=is_reacheabled, args=(line,))
            thr.start()
            threads.append(thr)

        for thr in threads:
            thr.join()


if __name__ == '__main__':
    main()
