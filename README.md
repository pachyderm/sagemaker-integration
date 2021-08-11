# Pachyderm + Sagemaker
This repo demonstrates how Pachyderm can be integrated with Sagemaker (and other AWS services). Specifically, Data Science teams who are developing pipelines with Sagemaker can follow this recipe to drive their Sagemaker pipelines with Pachyderm: Pachyderm will trigger runs, provide versioned input, and collect/version the output.

This adds versioning, provenance, incrementality, and data-driven pipelines (e.g. automated model retraining) to Sagemaker's feature set.

Repository content:

* `demo.ipynb`: step by step demo
* `dataset/`: contains a public customer churn dataset, to be used in the demo
* `CopyPipeline`/`TrainPipeline`: Docker Images used in the demo notebook; builds are available on the public Docker Hub.

