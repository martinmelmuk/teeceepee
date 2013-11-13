#!/usr/bin/env ipython

FAKE_IP = "10.0.4.4"
MAC_ADDR = "60:67:20:eb:7b:bc"
from scapy.all import send, Ether, ARP
import sys
import os


# The tests can't run as not-root
RUN = True
try:
    for _ in range(4):
        send(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(psrc=FAKE_IP, hwsrc=MAC_ADDR))
except:
    RUN = False

import time
import tcp
from tcp import TCPSocket
from tcp_listener import TCPListener

google_ip = "173.194.43.39"

def test_connect_google():
    if not RUN: return
    listener = TCPListener(FAKE_IP)
    conn = TCPSocket(listener)

    conn.connect(google_ip, 80)
    time.sleep(2)
    conn.close()
    time.sleep(2)
    assert False

def test_get_google_homepage():
    if not RUN: return
    payload = "GET / HTTP/1.0\r\n\r\n"

    listener = TCPListener(FAKE_IP)
    conn = TCPSocket(listener)

    conn.connect(google_ip, 80)
    time.sleep(2)
    conn.send(payload)
    time.sleep(3)
    conn.close()
    time.sleep(3)

