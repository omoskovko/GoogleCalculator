# Floodlight Controller
# See https://floodlight.atlassian.net/wiki/spaces/floodlightcontroller/pages/1343544/Installation+Guide
# for more information
#
# Build image using this Dockerfile
#    docker build -t moskovko/floodlight .
#
# Run container using this image:
#   docker run -it -p 6653:6653 -p 8080:8080 moskovko/floodlight

FROM openjdk:8
LABEL maintainer="masha.moskovko@gmail.com"

RUN apt-get update && \
    apt-get install -y software-properties-common maven git

RUN git clone https://github.com/floodlight/floodlight.git && \
    cd floodlight/ && git submodule init && git submodule update

WORKDIR /floodlight
RUN mvn package -DskipTests
# Remove -XX:PreBlockSpin=8 string from floodlight.sh
# because of error in java command line 
RUN sed -i 's/ -XX:PreBlockSpin=8//' ./floodlight.sh
RUN mkdir /var/lib/floodlight && chmod 777 /var/lib/floodlight

ENTRYPOINT ["/floodlight/floodlight.sh"]