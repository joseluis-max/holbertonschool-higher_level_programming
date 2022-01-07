#!/usr/bin/bash
# to get body size response
curl -s --head "$1" | head -n 5 | tail -n 1 | cut -d " "  -f 2
