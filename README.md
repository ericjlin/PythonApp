# Docker

Build the Application

``docker build -t app -f docker/Dockerfile .``

Run the Application

``docker run -v $PWD:/src app``

Cockroach DB Container Setup

``docker network create -d bridge app``

``docker run -d --name=roach1 --hostname=roach1 --net=app -p 26257:26257 -p 8080:8080 -p 5432:5432 -v $PWD/cockroach-data/roach1:/cockroach/cockroach-data  cockroachdb/cockroach start --insecure --join=roach1,roach2``

``docker run -d --name=roach2 --hostname=roach2 --net=app -v "$PWD/cockroach-data/roach2:/cockroach/cockroach-data" cockroachdb/cockroach start --insecure --join=roach1,roach2``

``docker exec -it roach1 ./cockroach init --insecure``


Running App with Network Bridge

``docker run -v $PWD:/src --network app app``
