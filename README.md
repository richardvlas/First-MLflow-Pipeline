# The First MLflow Pipeline
This repository demonstrates how to build a simple MLflow pipeline by connecting two components.

It contains two already-built components, one that downloads the data and one that performs some data processing: it creates and visualize 
a t-SNE projection with 2 components, then saves the dataframe with the t-SNE components added as columns. 

The task is to stitch these two components together in a pipeline.

## Project Structure

The following represents the structure of folders and files contained in the project after runing the pipeline.

| Note: A lot of files generated by wandb and Mlflow were removed to keep the repository clean. Only artifacts generated are kept.

```bash
.
├── MLproject
├── README.md
├── conda.yml
├── config.yaml
├── download_data
│   ├── MLproject
│   ├── conda.yml
│   └── download_data.py
├── environment.yml
├── main.py
└── process_data
    ├── MLproject
    ├── artifacts
    │   └── iris.csv:v0
    │       └── iris.csv
    ├── clean_data.csv
    ├── conda.yml
    └── run.py
```


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

## The Configuration
The parameters controlling the pipeline are defined in the `config.yaml` file defined in the root of the repository. We will use Hydra to manage this configuration file. 

Open this file and get familiar with its content. Remember: this file is only read by the `main.py` script (i.e., the pipeline) and its content is available with the go function in `main.py` as the config dictionary. For example, the name of the project is contained in the `project_name` key under the `main` section in the configuration file. It can be accessed from the `go` function as `config["main"]["project_name"]`.

> NOTE: do NOT hardcode any parameter when writing the pipeline. All the parameters should be accessed from the configuration file.

## Running the Pipeline
In order to run the pipeline when you are developing, you need to be in the root of the repository, then you can execute this command:

```bash
$ mlflow run .
```

This will run the entire pipeline.

You can override any other parameter in the configuration file using the Hydra syntax, by providing it as a `hydra_options` parameter. For example, say that we want to set the parameter main -> experiment_name to prod. This can be accomplished by running the pipeline again changing the name of the experiment from the command line as:

```bash
mlflow run . -P hydra_options="main.experiment_name=prod"
```

## Visualize the Pipeline
You can now go to W&B, go the Artifacts section, select an artifact and then click on Graph view tab. You will see a representation of your pipeline as:
   ![screenshot](first_pipeline.png "first pipeline")
