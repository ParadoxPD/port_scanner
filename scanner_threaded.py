import argparse
import socket
import threading


def connection_scan(target_ip, target_port):

    try:
        conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_socket.connect((target_ip, target_port))
        print(f"\t[+] {target_port}/tcp open.")

    except OSError:
        print(f"\t[-] {target_port}/tcp closed.")

    finally:
        conn_socket.close()


def port_scan(target, port_number):

    try:
        target_ip = socket.gethostbyname(target)

    except OSError:
        print(f"[^] Cannot resolve host {target_ip} : Unknown host ")
        return

    t = threading.Thread(target=connection_scan, args=(target_ip, port_number))
    t.start()


def argument_parser():
    parser = argparse.ArgumentParser(
        description="TCP port scanner. Accepts a hostname/IP address and list of ports toscan. Attempts to identify the service running on a port.")
    parser.add_argument('-u', "--host", nargs="?", help="Host IP address")
    parser.add_argument('-p', "--ports", nargs="?",
                        help="Comma-separated port list, such as '22,80,8080'")

    var_args = vars(parser.parse_args())

    return var_args


if __name__ == '__main__':
    try:
        user_args = argument_parser()
        host = user_args["host"]
        port_list = [int(x) for x in user_args["ports"].split(",")]
        print(f"[*] Scan results for {host} : ")
        for port in port_list:
            port_scan(host, port)

    except AttributeError:
        print("[x] Error, Please provide the command-line arguments before running\nUse -h/--help for help.")
