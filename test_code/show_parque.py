import pandas as pd
data = pd.read_parquet('/home/thuannd/Projects/MLOps-Competition-2023/data/train_data/phase-1/prob-2/test_x.parquet', engine='pyarrow')

print(data.iloc[5])