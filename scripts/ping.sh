#!/bin/bash
for i in `seq 100 105`;do
ping -c 1  192.168.0.$i  >>/dev/null && echo "192.168.0.$i is up" || echo "192.168.0.$i id down"
done
