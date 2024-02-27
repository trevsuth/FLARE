#!/bin/bash

# Assign the first command line argument to ENV_NAME
ENV_NAME="$1"

# Check if the environment variable ENV_NAME is empty
if [ -z "$ENV_NAME" ]; then
  echo "Usage: $0 <env_name>"
  exit 1
fi

# Check if the conda environment exists
env_exists=$(conda env list | grep "^$ENV_NAME\s")

if [ -n "$env_exists" ]; then
  echo "'$ENV_NAME' already exists"
else
  echo "Environment '$ENV_NAME' does not exist. Creating it with Python 3.10."
  conda create --name "$ENV_NAME" python=3.10 -y
fi
