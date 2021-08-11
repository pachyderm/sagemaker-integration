VERSION=0.0.1
IMAGE_BASE=winderresearch/example-pachyderm-copy-to-aws-s3

build:
	docker build . -t ${IMAGE_BASE}:${VERSION}

push: build
	docker push ${IMAGE_BASE}:${VERSION}

pull:
	docker pull 

run:
	docker run -it ${IMAGE_BASE}:${VERSION}