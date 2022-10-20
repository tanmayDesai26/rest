from __future__ import print_function
import grpc
import lab6_pb2_grpc as pb2_grpc
import lab6_pb2 as pb2
import time
import sys
import random
import base64



class Lab6Client(object):
    """
    Client for gRPC functionality
    """

    def __init__(self, host):
        self.host = host
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.Lab6Stub(self.channel)

    def add(self, first , second):
        message = pb2.addMsg(a=first,b=second)
        #print(f'{message}')
        return self.stub.DoAdd(message)
    
    def dotProduct(self):
        listA = []
        for i in range(0,2):
            randomNumber = random.random()
            listA.append(randomNumber)
        #print(listA)
        listB = []
        for i in range(0,2):
            randomNumber = random.random()
            listB.append(randomNumber)
        message = pb2.dotProductMsg(a=listA,b=listB)
        #print(f'{message}')
        return self.stub.DotProduct(message)
    
    
    def doRawImage(self):
        # prepare headers for http request
        rawImage = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
        message = pb2.rawImageMsg(img=rawImage)
        return self.stub.RawImage(message)
    
    def doJsonImage(self):
        img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
        encodedImage = base64.b64encode(img).decode('utf-8')
        message = pb2.jsonImageMsg(img=encodedImage)
        return self.stub.JsonImage(message)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <server ip> <cmd> <reps>")
        print(f"where <cmd> is one of add, rawImage, sum or jsonImage")
        print(f"and <reps> is the integer number of repititions for measurement")

    host = sys.argv[1]
    cmd = sys.argv[2]
    reps = int(sys.argv[3])
    client = Lab6Client(host)
    print(f"Running {reps} reps")
    if cmd == 'add':
        start = time.perf_counter()
        for x in range(reps):
            response = client.add(5,10)
        delta = ((time.perf_counter() - start)/reps)*1000
        print("Took", delta, "ms per operation")
    elif cmd == 'dotProduct':
        start = time.perf_counter()
        for x in range(reps):
            response = client.dotProduct()
        delta = ((time.perf_counter() - start)/reps)*1000
        print("Took", delta, "ms per operation")
    elif cmd == 'rawImage':
        start = time.perf_counter()
        for x in range(reps):
            response = client.doRawImage()
        delta = ((time.perf_counter() - start)/reps)*1000
        print("Took", delta, "ms per operation")
    elif cmd == 'jsonImage':
        start = time.perf_counter()
        for x in range(reps):
            response = client.doJsonImage()
        delta = ((time.perf_counter() - start)/reps)*1000
        print("Took", delta, "ms per operation")