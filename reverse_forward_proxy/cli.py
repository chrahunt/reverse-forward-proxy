import argparse
import logging

from .server import make_server


def enable_debug():
    logging.basicConfig(level=logging.DEBUG)
    requests_log = logging.getLogger('requests.packages.urllib3')
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

    from http.client import HTTPConnection, HTTPSConnection
    HTTPConnection.debuglevel = 2


def main():
    parser = argparse.ArgumentParser(description='reverse proxy for forward proxy')
    parser.add_argument('--proxy', required=True, help='forward proxy address, e.g. 192.168.1.2:8080')
    parser.add_argument('--listen-port', required=True, type=int, default=8080, help='host:port to bind to, for frontend')
    parser.add_argument('--cacert', help='CA cert path')
    parser.add_argument('--verbose', '-v', action='store_true', help='enable verbose logging')
    args = parser.parse_args()

    if args.verbose:
        enable_debug()

    address = ('', args.listen_port)
    server = make_server(address, args.proxy)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('Killed')
