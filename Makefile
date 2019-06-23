.PHONY: image

IMAGE = build/.image-build
IMAGE_NAME = chrahunt/reverse-forward-proxy

image: $(IMAGE);

$(IMAGE): build Dockerfile docker/entrypoint .dockerignore $(shell find reverse_forward_proxy)
	docker build -t $(IMAGE_NAME):SNAPSHOT .
	touch build/.image-build

build:
	mkdir build

run: $(IMAGE)
	docker run --rm -it $(IMAGE_NAME):SNAPSHOT

docker-test: $(IMAGE)
	cd docker && docker-compose up --build --force-recreate

get-port:
	@docker inspect docker_gateway_1 | jq -r '.[0].NetworkSettings.Ports["8080/tcp"][0].HostPort'
