.PHONY: build static-render live-render stop

CONTAINER ?= reveal-md-slides

build:
	docker build -t ${CONTAINER} .

stop:
	docker kill ${CONTAINER}

ifndef PRESENTATION_NUMBER
	$(error variable PRESENTATION_NUMBER is not set)
endif

PRESENTATION_PATH := $(shell find ${PRESENTATION_NUMBER}* -depth 0)

ifndef PRESENTATION_PATH
	$(error PRESENTATION_NUMBER ${PRESENTATION_NUMBER} is not in this directory)
endif

static-render: build
	docker run \
    --rm \
    -v $(shell pwd):/home \
    --entrypoint reveal-md \
    ${CONTAINER} \
    --template master.html \
    --css footer.css  \
    --static ${PRESENTATION_PATH} \
    ${PRESENTATION_PATH}/slides.md && \
		mv ${PRESENTATION_PATH}/slides.html ${PRESENTATION_PATH}/index.html

live-render: build
	docker run \
    --rm \
    -d \
    --name ${CONTAINER} \
    -p 1948:1948 \
    -v $(shell pwd):/home \
    --entrypoint reveal-md \
    ${CONTAINER} \
    --template master.html \
    --css footer.css  \
		--css base.css \
		--assets-dir assets \
    ${PRESENTATION_PATH}/slides.md
