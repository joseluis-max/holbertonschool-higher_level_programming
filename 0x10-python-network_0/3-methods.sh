#!/bin/bash
#takes in a URL and displays all HTTP methods the server will accept.
curl -s --head "$1" | grep 'Allow:' | cut -d " " -f2-
