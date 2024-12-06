#!/bin/bash
set -e

# Stop the running container (if any)
echo "Stopping..."
docker stop $(docker ps -a -q)
echo "Stopped all containers..."
