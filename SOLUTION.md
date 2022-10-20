# Timings for REST and GRPC
|Method | Local| Same-Zone| Different Region|
|:-: | :-: | :-: | :-: |
|REST add|2.51|3.17|276.96|
|gRPC add|0.67|   0.60|138.96|
|REST rawimg|4.38|9.20|1138.17|
|gRPC rawimg|8.15|10.52|187.80|
|REST dotproduct|3.27|3.30|277.85|
|gRPC dotproduct|0.59|   0.63|  138.91 |
|REST jsonimg|48.83|53.50|1288.99|
|gRPC jsonimg|24.03 |25.11|214.70|
|PING|0.048|0.374|136.510|


The results shows that grpc is much faster in every case. The grpc call, for the fist call is slower than the rest because during that call, it tries to establish the connection between client and server. But once the connection is established, the grpc call becomes very fast. While in the case of rest call, the connection is extablished for every call. the latency also plays role in the avg time because it takes time to send data from one VM to another VM and get the data back. 