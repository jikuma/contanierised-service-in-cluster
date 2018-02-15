# Steps to build and test docker image

## Build an image

docker build -t jikuma/simple-service .

## Run an image

docker run -p 5000:5000 jikuma/simple-service

## Check if service is running

docker ps

output:

CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                    NAMES

e3db66dd32fb        jikuma/simple-service   "python app.py"     38 seconds ago      Up 37 seconds       0.0.0.0:5000->5000/tcp   vigilant_mayer

## Stop the service

docker stop e3db66dd32fb




