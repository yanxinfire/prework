VERSION ?= v1.0.0

IMAGEREGISTRY ?= yanxinfire
IMAGENAME ?= api-server
IMAGETAG ?= latest
IMG ?= $(IMAGEREGISTRY)/$(IMAGENAME):$(IMAGETAG)

all: docker-build

docker-build:
	docker build -t ${IMG} .