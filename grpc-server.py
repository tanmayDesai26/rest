import grpc
import lab6_pb2_grpc as pb2_grpc
import lab6_pb2 as pb2
from concurrent import futures
import time
import numpy as np
import base64
import io
from PIL import Image


class Lab6Server(pb2_grpc.Lab6Servicer):
    
    def __init__(self, *args, **kwargs):
        pass
    
    def DoAdd(self, request, context):
        a = request.a
        b = request.b
        result = {'sum' : a + b}
        return pb2.addReply(**result)

    def DotProduct(self, request, context):
        a = request.a
        b = request.b
        dotproduct = np.dot(a,b)
        result = {'dotproduct' : dotproduct}
        return pb2.dotProductReply(**result)
    
    def RawImage(self, request, context):
        imageBytes = request.img
        #print(type(imageBytes))
        try:
            ioBuffer = io.BytesIO(imageBytes)
            print(ioBuffer)
            img = Image.open(ioBuffer)
        # build a response dict to send back to client
            result = {
                'width' : img.size[0],
                'height' : img.size[1]
                }
        except:
            print("Error")
            result = { 'width' : 0, 'height' : 0}
        return pb2.imageReply(**result)
    
    def JsonImage(self, request, context):
        encodedImage = request.img
        #print(type(encodedImage))
        decodedString = base64.b64decode(encodedImage)
        #print(type(decodedString))
        try:
            ioBuffer = io.BytesIO(decodedString)
            img = Image.open(ioBuffer)
        # build a response dict to send back to client
            result = {
                'width' : img.size[0],
                'height' : img.size[1]
                }
        except:
            print("Error")
            result = { 'width' : 0, 'height' : 0}
        return pb2.imageReply(**result)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_Lab6Servicer_to_server(Lab6Server(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    
    
if __name__ == '__main__':
    serve()