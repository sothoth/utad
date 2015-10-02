#!/bin/bash

# Integration tests


WEB_IP=web


python tests.py
if [ $? -ne 0 ]; then
    echo "Unit tests failed!"
    exit 1
fi

if curl http://${WEB_IP}:80 | grep -q '<b>Visits:</b> '; then
  echo "Tests passed!"
  exit 1
fi

echo "Integration tests failed!"
exit 1
