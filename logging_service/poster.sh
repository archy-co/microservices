#!/bin/bash

# Send post request to localhost port 5000 with msg "hello"

curl -X POST -d "msg=hello" http://localhost:5000
