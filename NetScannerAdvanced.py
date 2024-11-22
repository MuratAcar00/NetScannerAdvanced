import scapy.all as scapy
import optparse

#1-Arp_request
#2-Broadcast
#3-Response

def getUserInput():

    parseObject = optparse.OptionParser()
    parseObject.add_option("-i", "--ipaddress",dest = "ipAddress", help = "Enter ip address")
    (userInputs, arguments) = parseObject.parse_args()

    if not userInputs.ipAddress:
        print("Enter ip address")

    return userInputs


def scanMyNetwork(ip):

    #Agda bu ip adresini bulmaya calisiyor
    arpRequestPacket = scapy.ARP(pdst = ip)

    #Scapy kutuphanesinde ki help metodu gibi
    #scapy.ls(scapy.ARP())

    broadcastPacket = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())

    combinedPacket = broadcastPacket/arpRequestPacket

    (answeredList, unansweredList) = scapy.srp(combinedPacket, timeout = 1)

    #Cevap veren iplerin ozeti
    answeredList.summary()

userIpAddress = getUserInput()
scanMyNetwork(userIpAddress.ipAddress)