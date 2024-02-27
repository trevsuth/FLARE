# FLARE learning

Taken from https://github.com/ayushtues/FLARE_from_scratch/blob/main/main.py

Made using python3.10
## Setup

### Setup using conda environments
run the following command
``` 
./setup_env.sh
```

### Setup using docker
run the following
```
docker build -t flare_image .
docker run --name flare_container -it flare_image
```