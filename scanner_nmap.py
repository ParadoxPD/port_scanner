import argparse
import nmap


def nmap_scan(target, port_number):
    nm = nmap.PortScanner()
    nm = nm.scan(target, port_number)
    print(nm)
    state = nm['nmap']['tcp'][int(port_number)]['state']
    result = f'tcp/{port_number} {state}'

    return result


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
        port_list = user_args["ports"].split(",")
        print(f"[*] Scan results for {host} : ")
        for port in port_list:
            print(nmap_scan(host, port))

    except AttributeError:
        print("[x] Error, Please provide the command-line arguments before running\nUse -h/--help for help.")
