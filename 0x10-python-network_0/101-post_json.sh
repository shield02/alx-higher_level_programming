#!/bin/bash
# send JSON POST request to URL passed as the first argument
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
