import grpc
import Unary.addrpc.add_pb2_grpc as add_pb2_grpc
import Unary.addrpc.add_pb2 as add_pb2


class Client(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50052

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = add_pb2_grpc.AddStub(self.channel)

    def get_sum(self, a, b):
        """
        Client function to call the rpc for GetServerResponse
        """
        #dummy test a>b
        if a>b:
            return True
        numbers = add_pb2.Numbers(a=a,b=b)

        print(f'{numbers}')
        return self.stub.GetAddResult(numbers)


if __name__ == '__main__':
    client = Client()
    for i in range(5):
      result = client.get_sum(i, 2)
      i=i+1
      print(f'{result}')
