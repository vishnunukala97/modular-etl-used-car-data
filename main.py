from extract import extract_all_files
from transform import transform
from load import load_data
from log import log_process

import os
print("Current Working Directory:", os.getcwd())


log_process("ETL process started")

log_process("Extract Phase started")
data = extract_all_files()
log_process("Extract Phase completed")

print("Extracted data preview:")
print(data.head())
print(f"Shape of data: {data.shape}")

log_process("Transform Phase started")
transformed_data = transform(data)
log_process("Transform Phase completed")

log_process("Load Phase started")
load_data("transformed_data.csv", transformed_data)
log_process("Load Phase completed")

log_process("ETL process completed")