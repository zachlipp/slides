FROM node:12.13-buster-slim

RUN apt-get update && \
    apt-get install -y git

RUN git clone https://github.com/hakimel/reveal.js.git

RUN cd reveal.js

RUN npm install && \
    npm install -g reveal-md && \
    npm install puppeteer

WORKDIR home
