from fastapi import FastAPI
import scapy.all as scapy

app = FastAPI()

@app.get("/")
def home():
    return "API - DISPOSITIVOS NA REDE"

@app.get("/connections")
def con():
    x = 0
    request = scapy.ARP()

    request.pdst = '192.168.10.0/24'
    broadcast = scapy.Ether()

    broadcast.dst = 'ff:ff:ff:ff:ff:ff'

    request_broadcast = broadcast / request
    clients = scapy.srp(request_broadcast, timeout=2)[0]
    ip = []
    for element in clients:
        ip.append(element[1].psrc)
    print(ip)
    return ip