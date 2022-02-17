import mlflow
import os
import hydra
from omegaconf import DictConfig


# This automatically reads in the configuration file config.yaml
# and makes it available as function argument - config
@hydra.main(config_name='config')
def go(config: DictConfig):

    # Setup the wandb project & experiment. All runs will be grouped 
    # under this name
    os.environ["WANDB_PROJECT"] = config["main"]["project_name"]
    os.environ["WANDB_RUN_GROUP"] = config["main"]["experiment_name"]

    # You can get the path at the root of the MLflow project with this:
    root_path = hydra.utils.get_original_cwd()

    # Running 1. component
    _ = mlflow.run(
        uri = os.path.join(root_path, "download_data"),
        entry_point = "main",
        parameters = {
            "file_url": config["data"]["file_url"],
            "artifact_name": "iris.csv",
            "artifact_type": "raw_data",
            "artifact_description": "Input data"
        },
    )

    # Running 2. component
    _ = mlflow.run(
        uri = os.path.join(root_path, "process_data"),
        entry_point = "main",
        parameters = {
            "input_artifact": "iris.csv:latest",
            "artifact_name": "clean_data.csv",
            "artifact_type": "processed_data",
            "artifact_description": "Cleaned data"
        }
    )


if __name__ == "__main__":
    # Since we are using hydra in this  main script, we do not use argparse
    # this function is invoked without any argument. The config argument is 
    # added by the decorator, which reads the configuration file specified 
    # by config_name. Using Using config_name="config" means that Hydra is 
    # going to look for the configuration in config.yaml
    go()
