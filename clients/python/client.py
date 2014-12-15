import argparse
import time

from weltamdraht import WeltamDraht
from weltamdraht.ttypes import WAD_Signature
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol


def create_client(config_path):
    """ Creates a client to be used when connecting to the WeltamDraht server.
    :param config_path: Path to configuration file
    :type: str
    :return: WeltamDraht.Client
    """
    transport = TSocket.TSocket(host="localhost", port=9999, unix_socket=None)
    transport = TTransport.TFramedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    transport.open()
    return WeltamDraht.Client(protocol)


def do_requests(client, operation, api_key):
    deltas = []
    while True:
        req = queue.get()
        if not req:
            break

        start_time = time.time()
        op = ClientOperation(client, True)
        op.do_operation(operation, api_key)
        diff = time.time() - start_time
        deltas.append(diff)
    return deltas


def client_func(config, operation, api_key):
    client = create_client(config)
    reply = do_requests(client, operation, api_key)
    del client
    return reply


class ClientOperation(object):
    def __init__(self, client, benchmark=False):
        """
        The operations that a client can use to communicate with the WeltamDraht
        :param client: The client that is used to connect to the WeltamDraht server.
        :type: WeltamDraht.Client
        :return:
        """
        self.client = client

    def do_operation(self, operation, api_key):
        """
        You can specify which operation to do with a string.
        :param operation: The method of this object.
        :type: String
        :param api_key: The API key to use.
        :type: String
        """
        start_time = time.time()
        method = getattr(self, operation)
        result = method(api_key)
        timedelta = time.time() - start_time
        print "The '%s' operation took %d ms." % (operation, timedelta)
        print "The result:\n", result

    def ping(self, api_key):
        """
        Ping the WeltamDraht server.
        :param api_key:
        :type: String
        """
        signature = WAD_Signature()
        return self.client.ping(signature, 'test client')


EXAMPLES = """Examples:
ping:          -c scalerib_vzn.ini -pi
"""


def script_main():
    """
    Main script that takes arguments to either test the WeltamDraht or to benchmark it.
    """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description="WetlamDraht Benchmark Tool",
                                     epilog=EXAMPLES)
    parser.add_argument("-c", "--config", type=str, required=True, help="The configuration file to use.")
    parser.add_argument("-k", "--key", type=str, required=True, help="WeltamDraht user Key.")
    op_group = parser.add_mutually_exclusive_group(required=True)
    op_group.add_argument("-pi", "--ping", action='store_true', help="Call ping.")

    args = parser.parse_args()

    operation = None
    if args.ping:
        operation = 'ping'

        op = ClientOperation(create_client(args.config))
        op.do_operation(operation, args.key)

if __name__ == '__main__':
    script_main()
