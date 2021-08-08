# How to Use

```
   1) Set file permission , chmod 777 analysis_pcap_arp
   
   2) python3 analysis_pcap_arp --pcap [pcap_file]   # Print detailed information
   
   3) python3 analysis_pcap_arp --min [pcap_file]  # Print less information
   
 ```
 
# Program Logic

```
  Reading the pcap file using scapy RawPcapReader , check if packet is ARP request / Response , 
  if yes then print ARP request and response and count the number of
  packets . script will also check if a destination IP failed to reply back
  
```

# How to find your Router IP and MAC address

```
check the ARP request packet
open Ethernet part , check destination , it will be FF:FF:FF:FF:FF:FF ( Broadcast )
check destination IP in ARP part , it will be your default gateway / router's IP address
```

![ip_route](https://user-images.githubusercontent.com/35332582/128627688-3f63d1d9-6b64-48f3-969b-1a99444e0a70.png)

```
check the ARP response packet
To find Router's MAC Adress check source MAC address in ARP Part
```
![mac_route](https://user-images.githubusercontent.com/35332582/128627726-4b4684ea-2fe1-49ba-8493-19cfe9ffeb0f.png)



# Note


``` 
  Request Packet     : White Color
  
  Response Packet    : Green Color
  
  Error with Packet  : Red Color
  
```
# Sample Video




https://user-images.githubusercontent.com/35332582/128629067-cbed2133-fa62-4192-86ec-851f1f40976e.mp4



