VERSION=0.0.1
IMAGE_BASE=winderresearch/example-pachyderm-train-sagemaker

build:
	docker build . -t ${IMAGE_BASE}:${VERSION}

push: build
	docker push ${IMAGE_BASE}:${VERSION}

pull:
	docker pull 

run:
	docker run -it ${IMAGE_BASE}:${VERSION}