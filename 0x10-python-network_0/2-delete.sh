#!/bin/bash
# ends a DELETE request to the URL passed as the first argument \
# and displays the body of the response
curl -s -L -X DELETE "$1"
