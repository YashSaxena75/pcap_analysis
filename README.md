# How to Use

```
   1) Set file permission , chmod 777 analysis_pcap_arp
   
   2) ./analysis_pcap_arp --pcap [pcap_file]   # Print detailed information
   
   3) ./analysis_pcap_arp --min [pcap_file]  # Print less information
   
 ```
 
# Program Logic

```
  Reading the pcap file using scapy RawPcapReader , check if packet is ARP request / Response , 
  if yes then print ARP request and response and count the number of
  packets . script will also check if a destination IP failed to reply back
  
```

# Note

``` 
  Request Packet     : Blue Color
  
  Response Packet    : Green Color
  
  Error with Packet  : Red Color
  
```
# Sample Video


https://user-images.githubusercontent.com/35332582/128598556-2129ce6d-9ec2-4782-9dab-f82a3588000e.mp4


