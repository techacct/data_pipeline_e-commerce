import subprocess
from generate_data import generate_and_save_data
from load_data import load_data

# Define the command to execute the script
command = ['python', r'C:\\Users\\ademo\data_ppeline_e-commerce\\read_csv.py']

# Run the script
generate_and_save_data()
subprocess.call(command)
load_data()
