#!/bin/bash
# Get the byte size of HTTP response for  URL.
curl -s "$1" | wc -c