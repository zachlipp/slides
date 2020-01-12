.PHONY: build static-render live-render stop

CONTAINER ?= reveal-md-slides

build:
	docker build -t ${CONTAINER} .

stop:
	docker kill ${CONTAINER}

variable-check:
	# Must pass PRESENTATION_NUMBER from command line
	ifndef PRESENTATION_NUMBER
		$(error variable PRESENTATION_NUMBER is not set)
	endif
	
	PRESENTATION_PATH := $(shell find ${PRESENTATION_NUMBER}* -depth 0)
	
	# The selected slide must actually exist
	ifndef PRESENTATION_PATH
		$(error PRESENTATION_NUMBER ${PRESENTATION_NUMBER} is not in this directory)
	endif

static-render: build variable-check
	docker run \
    --rm \
    -v $(shell pwd):/home \
    --entrypoint reveal-md \
    ${CONTAINER} \
    --template master.html \
    --css footer.css  \
    --static ${PRESENTATION_PATH}/_site \
    --static-dirs ${PRESENTATION_PATH}/_assets \
    --static-dirs ${PRESENTATION_PATH}/figs \
    ${PRESENTATION_PATH}/slides.md

live-render: build variable-check
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
    ${PRESENTATION_PATH}/slides.md
