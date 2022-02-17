# The First MLflow Pipeline
This repository demonstrates how to build a simple MLflow pipeline by connecting two components.

It contains two already-built components, one that downloads the data and one that performs some data processing: it creates and visualize 
a t-SNE projection with 2 components, then saves the dataframe with the t-SNE components added as columns. 

The task is to stitch these two components together in a pipeline.

## Preliminary steps
### Clone the Project
Clone this repository locally so that you can run it:

```bash
$ git clone https://github.com/richardvlas/First-MLflow-Pipeline.git
```
and go into the repository:

```bash
$ cd First-MLflow-Pipeline
```

### Create environment

Make sure to have conda installed and ready, then create a new environment using the `environment.yml` file provided in the root of the repository and activate it:

```bash
$ conda env create -f environment.yml
$ conda activate first_mlflow_pipeline 
```

### Get API key for Weights and Biases

Let's make sure you are logged in to Weights & Biases. Get your API key from W&B by going to https://wandb.ai/authorize and click on the + icon (copy to clipboard), then paste your key into this command:

```bash
$ wandb login [your API key]
```

You should see a message similar to:

```
wandb: Appending key for api.wandb.ai to your netrc file: /home/[your username]/.netrc
```



