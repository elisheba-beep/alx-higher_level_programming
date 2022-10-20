#!/bin/bash
# takes in a URL, sends a GET request and displays the response.
curl -sX GET -H "X-School-User-Id: 98" "$1"
