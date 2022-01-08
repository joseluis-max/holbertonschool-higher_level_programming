#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
status=$(curl -s -o /dev/null --head -w "%{http_code}" -X GET "$1")
if [ "$status" == "200" ]; then
    curl -s "$1"
fi
