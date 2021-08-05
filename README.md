# How to Use

```
   1) Set file permission , chmod 777 arp.py
  
   2) ./analysis_pcap_arp --pcap [pcap_file]   # Print detailed information
   
   3) ./analysis_pcap_arp --min [pcap_file]  # Print less information
   
 ```
 
# Program Logic

```
  Reading the pcap file using scapy RawPcapReader , check if packet is ARP request / Response , 
  if yes then print ARP request and response and count the numbers of
  packets . script will also check if a destination IP failed to reply back
  
```

# Note

``` 
  Request Packet     : Blue Color
  
  Respomse Packet    : Green Color
  
  Error with Packet  : Red Color
  
```
