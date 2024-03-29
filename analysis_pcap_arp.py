# import necessary packages

import optparse
import os
from time import sleep
import sys
from scapy.all import *
from colorama import Fore , Style


os.system("id")
#function to process less information

def pcap_min(f_name):

    arpp = 0
    req  = 0
    previp = []
    prevop = []
    prevsrc =  []

    print()
    print('Analaysing ' + f_name )


    pkts_data = rdpcap(f_name)
    for i in range(0,len(pkts_data)):
        try:
            if pkts_data[i]['Ethernet'].type==0x0806: # Process only if it is an ARP packet
                arpp += 1
                previp.append(pkts_data[i]['ARP'].pdst)
                prevop.append(pkts_data[i]['ARP'].op)
                prevsrc.append(pkts_data[i]['ARP'].psrc)

                if arpp >= 2 and previp[arpp-2] == pkts_data[i]['ARP'].pdst and pkts_data[i]['ARP'].op==1 and pkts_data[i]['ARP'].op==prevop[arpp-2] and pkts_data[i]['ARP'].psrc==prevsrc[arpp-2]:
                    req += 1

                elif previp[arpp-2]!=pkts_data[i]['ARP'].pdst and pkts_data[i]['ARP'].op == 1:
                    req = 0
                    

                elif prevsrc[arpp-2]!=pkts_data[i]['ARP'].psrc and pkts_data[i]['ARP'].op == 1:
                    req = 0

                elif previp[arpp-2]!=pkts_data[i]['ARP'].pdst and pkts_data[i]['ARP'].op == 2:
                    req = 0

                if req<1 and pkts_data[i]['ARP'].op == 1:
                    #display the packet only if request / response was successful
                    print(Fore.WHITE)
                    print("Ethernet MAC : " , pkts_data[i]['Ethernet'].dst , "\n")
                    print("Source IP : " , pkts_data[i]['ARP'].psrc , "\n")
                    print("Destination IP : " , pkts_data[i]['ARP'].pdst , "\n")
                    print("Source MAC : ",pkts_data[i]['ARP'].hwsrc,"\n")
                    print("Destination MAC : ",pkts_data[i]['ARP'].hwdst,"\n")
                    print(Style.RESET_ALL)

                elif req<1 and pkts_data[i]['ARP'].op == 2:
                    print(Fore.GREEN)
                    print("Source IP : " , pkts_data[i]['ARP'].psrc , "\n")
                    print("Destination IP : " , pkts_data[i]['ARP'].pdst , "\n")
                    print("Source MAC : " , pkts_data[i]['ARP'].hwsrc , "\n")
                    print(Style.RESET_ALL)
                    print("_______________________________________________________")

                else:
                    print(Fore.RED)
                    print(pkt.pdst,"didn't replied back")
                    print(Style.RESET_ALL)

        except Exception as e:
            continue
    print("\n\nProcessed total {} ARP packets".format(arpp))


# function to process detailed information

def pcap_analyses(file_name):

    arpp = 0
    req  = 0
    previp = []
    prevop = []
    prevsrc =  []

    print()
    print('Analaysing ' + file_name )


    pkts_data = rdpcap(file_name)
    for i in range(0,len(pkts_data)):
        try:
            if pkts_data[i]['Ethernet'].type==0x0806: # Process only if it is an ARP packet
                arpp += 1
                previp.append(pkts_data[i]['ARP'].pdst)
                prevop.append(pkts_data[i]['ARP'].op)
                prevsrc.append(pkts_data[i]['ARP'].psrc)

                if arpp >= 2 and previp[arpp-2] == pkts_data[i]['ARP'].pdst and pkts_data[i]['ARP'].op==1 and pkts_data[i]['ARP'].op==prevop[arpp-2] and pkts_data[i]['ARP'].psrc==prevsrc[arpp-2]:
                    req += 1

                elif previp[arpp-2]!=pkts_data[i]['ARP'].pdst and pkts_data[i]['ARP'].op == 1:
                    req = 0
                    

                elif prevsrc[arpp-2]!=pkts_data[i]['ARP'].psrc and pkts_data[i]['ARP'].op == 1:
                    req = 0

                elif previp[arpp-2]!=pkts_data[i]['ARP'].pdst and pkts_data[i]['ARP'].op == 2:
                    req = 0

                print()

                if req<1 and pkts_data[i]['ARP'].op == 1:

                    print(Fore.WHITE)
                    print("request")
                    #display the packet only if request / response was successful
                    print(pkts_data[i].show())
                    print(Style.RESET_ALL)

                elif req<1 and pkts_data[i]['ARP'].op == 2:
                    print(Fore.GREEN)
                    #display the packet only if request / response was successful
                    print(pkts_data[i].show())
                    print(Style.RESET_ALL)
                    print("_______________________________________________________")

                else:
                    print(Fore.RED)
                    print(pkts_data[i]['ARP'].pdst,"didn't replied back")
                    print(Style.RESET_ALL)

        except Exception as e:
            continue

    print("\n\n Processed total {} ARP packets".format(arpp))

# main code

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option("--pcap", dest="file_name", help="[pcap-file-name]")
    parser.add_option("--min" ,dest="f_name" ,help="[pcap-file-name]")
    (options,arguments)=parser.parse_args()

    if not options.file_name and not options.f_name:
        parser.error("[-] missing argument")

    else:
        if options.file_name:

            if os.path.isfile(options.file_name):
                pcap_analyses(options.file_name)

            else:
                print("\nFile doesn't exist\n")

        elif options.f_name:

            if os.path.isfile(options.f_name):
                pcap_min(options.f_name)

            else:
                print("\nFile doesn't exist\n")

    sys.exit(0)
