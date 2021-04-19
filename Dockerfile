FROM node:12.13-buster-slim

RUN apt-get update && \
    apt-get install -y git

RUN git clone https://github.com/hakimel/reveal.js.git && \
    cd reveal.js && \
    git fetch --all --tags && \
    git checkout 4.1.0

RUN npm install && \
    npm install -g reveal-md@4.2.0 && \
    npm install puppeteer@7.0.0

WORKDIR home
