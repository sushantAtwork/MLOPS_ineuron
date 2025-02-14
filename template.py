import logging
import os
from pathlib import Path

list_of_files = [

    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_evalution.py",
    "src/components/model_trainer.py",
    "src/data_transformation.py",
    "src/model_trainer.py",
    "src/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/prediction_pipeline.py"
    "src/pipeline/training_pipeline.py",
    "src/utils/utils.py",
    "src/utils/__init__.py",
    "src/logger/logging.py",
    "src/exception/pytest/unit/__init__.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirments.txt"
    "requirments.dev.txt",
    "setup.py",
    "pyproject.toml",
    "tox.ini",
    "setup.cfg",
    "experiment/experiments.ipynb",


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) # this will split directory and filename : dir ->  a/b and filename ->  c.txt
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory : {filedir} for file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file.

