#!/bin/bash
#takes in URL, sends a POST request to the URL and displays the body of the respose
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
