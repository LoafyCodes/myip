#!/bin/bash
OUTPUT="$(curl -s ifconfig.me)"
echo "Your external IP is: ${OUTPUT}"
