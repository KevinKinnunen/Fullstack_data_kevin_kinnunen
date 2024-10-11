from pathlib import Path  # pathlib to work with file and dir paths
from shutil import copytree, rmtree  # copytree to copy dirs, rmtree to remove dirs

raw_data_path = Path(__file__).parent / "raw_data"  # path to the raw_data dir from the parent of the current file's dir
cleaned_data_path = Path(__file__).parent / "cleaned_data"  # path to the cleaned_data dir from the parent of the current file's dir

if cleaned_data_path.is_dir():  # if the cleaned_data_path dir exists, remove it using rmtree to avoid duplication of files
    rmtree(cleaned_data_path)

cleaned_data_path.mkdir(parents=True, exist_ok=True)  # create the cleaned_data_path dir 

for folder in raw_data_path.iterdir():  # iterate over each folder in the raw_data_path dir
    new_name = folder.name.split()[0]  # extract the first part of the folder name by splitting on whitespace
    copytree(folder, cleaned_data_path / new_name)  # copy the folder to cleaned_data_path with the new formatted name
