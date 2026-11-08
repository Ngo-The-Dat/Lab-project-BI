import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

@data_loader
def load_data_from_file(*args, **kwargs):
    # Đường dẫn file bên trong container (/home/src là thư mục Lab-project-BI)
    file_path = '/home/src/dataset/Yellow Taxi Trip Record Data/2024/yellow_tripdata_2024-01.parquet' 
    df = pd.read_parquet(file_path)
    return df