## Proxyless gRPC service discovery using xDS
## xDS enabled Dynamic Discovery - Scalable and Resilient 


Thanks to gRPC group for enabling xDS. 

A working example of xDS control place server, with gRPC client and server.


This repository provides a control plane (xDS server) and example gRPC client and server. 
The intent of creating this repository is to provide a working example of XDS with capabilities like:
  a. Dynamic discovery - gRPC server registration.
  b. Management of resources.
  c. Static loading of service provider (aka gRPC server).
  d. And more (refer Service_Discovery folder).


I will keep updating this repo with new xDS capabilities


1. High Level View
![alt text](HLD1_APIS.png)

2. xDS Resources
![alt text](HLD_Bootstrap_Resources.png)

3. xDS Routing Control
![alt text](HLD_Resource_Routing.png)


### Reference:
  * [Envoy xDs protocol](https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol)
  * [Envoy xDS overview](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/operatons/dynamic_configuration)
  * [Envoyproxy/go-control-plane](https://github.com/envoyproxy/go-control-plane/tree/main) Right now v3 is the latest. 
  * [Proto](https://github.com/envoyproxy/go-control-plane/tree/main/envoy/config) - Listener, Route, etc.
  * [Load Balancing in gRPC](https://github.com/grpc/proposal/blob/master/A27-xds-global-load-balancing.md)
  * [xDS failover - Federation](https://github.com/grpc/proposal/blob/master/A47-xds-federation.md)
  * [gRPC](https://github.com/grpc/grpc)
