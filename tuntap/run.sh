#!/bin/sh

./tuntap.sh tuntap.py

sudo ip addr add 192.168.0.1/24 dev tun0
sudo ip link set up dev tun0
