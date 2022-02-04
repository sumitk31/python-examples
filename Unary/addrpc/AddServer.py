import grpc
import Unary.addrpc.add_pb2_grpc as add_pb2_grpc
import Unary.addrpc.add_pb2 as add_pb2
from concurrent import futures

class AddService(add_pb2_grpc.AddServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetAddResult(self, request, context):
        num1 = request.a
        num2 = request.b
        print(request)
        sum = num1 + num2
        response = {'sum':sum}
        return add_pb2.AddResult(**response)


def serve():
    #server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_pb2_grpc.add_AddServicer_to_server(AddService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
