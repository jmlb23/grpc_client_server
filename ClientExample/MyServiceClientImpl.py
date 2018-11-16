
import grpc
import proto.MyService_pb2
import proto.MyService_pb2_grpc

channel = grpc.insecure_channel('localhost:8888')
p = proto.MyService_pb2_grpc.MyServiceStub(channel)
x= proto.MyService_pb2.Request(id=1)
print(p.Search(x))

