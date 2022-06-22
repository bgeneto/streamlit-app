# streamlit-app

Bootstrap your first [Streamlit](https://streamlit.io) in seconds 
using this docker container with dependencies like pandas, numpy, matplotlib, plotly... already installed.

# Instructions 

## Clone this repo

```bash
git clone https://github.com/bgeneto/streamlit-app.git
```

## Build the base image

First you need to build the "streamlit-base" docker image. 
The proporse of this image is to serve as a base image to all your 
deployed streamlit app containers.

```bash
cd streamlit-app/streamlit-base
./build
```

If you don't have a localhost docker registry running, 
then issue the following command instead to avoid uploading this image to your local registry: 

```bash
cd streamlit-app/streamlit-base
./build --no-registry
```

You can also edit files `packages.txt` and `requirements.txt` to add the packages and 
software that is required to your container. 

## Build your app image

Now build the main app image/container. Edit the `.env` file in the root dir and then call docker compose. 
The provided `docker-compose.yml` file uses [autoheal](https://github.com/willfarrell/docker-autoheal) to monitor container status. 

```
cd .. 
docker compose up 
``` 



