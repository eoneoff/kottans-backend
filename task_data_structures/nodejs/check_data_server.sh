#!/bin/bash

echo "Test requests started"

curl -d '{"data": "somedata"}' -H "Content-Type: application/json" http://localhost:8000/list
curl -d '{"data": "moredata"}' -H "Content-Type: application/json" http://localhost:8000/list
curl http://localhost:8000/list
echo ""
curl -d '{"data": 20, "successor": "somedata"}' -H "Content-Type: application/json" http://localhost:8000/list
curl http://localhost:8000/list
echo ""
curl -X "DELETE" -d '{"data":"somedata"}' -H "Content-Type: application/json" http://localhost:8000/list
curl http://localhost:8000/list
echo ""

curl -d '{"data":1}' -H "Content-Type: application/json" http://localhost:8000/stack
curl -d '{"data":2}' -H "Content-Type: application/json" http://localhost:8000/stack
curl -d '{"data":3}' -H "Content-Type: application/json" http://localhost:8000/stack
curl -X "DELETE" http://localhost:8000/stack
echo ""
curl -X "DELETE" http://localhost:8000/stack
echo ""