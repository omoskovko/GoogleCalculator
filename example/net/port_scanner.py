import argparse
import socket
from colorama import init, Fore
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

init()

GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

N_THREADS = 5


def port_scan(port):
    res = ""
    try:
        s = socket.socket()
        s.connect(port)
    except:
        # res = f"{GRAY}{port[0]:15}:{port[1]:5} is closed {RESET}"
        # print(res)
        pass
    else:
        res = f"{GREEN}{port[0]:15}:{port[1]:5} is open {RESET}"
        print(res)
    finally:
        s.close()

    return res


def main(ports):
    with ThreadPoolExecutor(max_workers=N_THREADS) as executor:
        # with ProcessPoolExecutor() as executor:
        ports_list = [executor.submit(port_scan, p) for p in ports]
        # for worker in ports:
        #    executor.submit(port_scan, worker)
    # print([p.result() for p in ports_list if p.result()])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fast port scanner")
    parser.add_argument("--host", dest="host", help="Host to scann.")
    parser.add_argument(
        "--ports",
        "-p",
        dest="port_range",
        default="1-65535",
        help="Ports to scann, default is 1-65535 (all ports)",
    )
    args = parser.parse_args()
    host, port_range = args.host, args.port_range
    ports = [(host, p) for p in range(*[int(v) for v in port_range.split("-")])]
    main(ports)
