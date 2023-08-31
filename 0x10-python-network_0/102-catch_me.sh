#!/bin/bash
# send a request to 0.0.0.0:5000/catch_me and get a response with a message 'You got me!'
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool" -d "user_id=98"
