#!/bin/bash
# to get body size response
curl -s --head "$1" | grep 'Content-Length' | cut -d " " -f 2
