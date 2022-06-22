# streamlit-app

Bootstrap your first [Streamlit](https://streamlit.io) web application in seconds 
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
then issue the following command instead to avoid uploading this image to a non-existing local registry: 

```bash
./build --no-reg
```

You can also edit files `packages.txt` and `requirements.txt` to add the packages and 
softwares that are required in your container. 

## Build your app image

Now we are ready to build the main app image/container. 
But first edit the `.env` file in the root dir and then call docker compose. 

```
cd .. 
docker compose up 
```

 > **_Note:_**
The provided `docker-compose.yml` are ready to use but it depends on [autoheal](https://github.com/willfarrell/docker-autoheal) to monitor your streamlit container status. Just remember to run the autoheal container beforehand with `AUTOHEAL_CONTAINER_LABEL=autoheal`.


