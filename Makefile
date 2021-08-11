
build:
	make -C TrainPipeline build
	make -C CopyPipeline build

push: build
	make -C TrainPipeline push
	make -C CopyPipeline push