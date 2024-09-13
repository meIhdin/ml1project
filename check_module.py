import os

# Check if 'src/ml1project' directory exists
project_root = os.path.abspath(os.getcwd())  # Get the current working directory
ml1project_path = os.path.join(project_root, "src", "ml1project")

if os.path.isdir(ml1project_path):
    print(f"'{ml1project_path}' exists.")
else:
    print(f"'{ml1project_path}' does not exist.")

# Check if it's importable
try:
    from src.ml1project import logger
    print("src.ml1project is importable.")
except ModuleNotFoundError:
    print("src.ml1project is not importable.")


import os

# Define the path to the directory
project_root = os.path.abspath(os.getcwd())  # Get the current working directory
ml1project_dir = os.path.join(project_root, "src", "ml1project")
init_file_path = os.path.join(ml1project_dir, "__init__.py")

# Check if the directory exists
if os.path.isdir(ml1project_dir):
    print(f"Directory '{ml1project_dir}' exists.")
else:
    print(f"Directory '{ml1project_dir}' does not exist.")

# Check if __init__.py exists in the directory
if os.path.isfile(init_file_path):
    print(f"File '__init__.py' exists in '{ml1project_dir}'.")
else:
    print(f"File '__init__.py' does not exist in '{ml1project_dir}'.")
