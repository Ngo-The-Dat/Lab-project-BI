import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@transformer
def transform(data, *args, **kwargs):
    # Lọc bỏ các chuyến đi có số hành khách <= 0 hoặc tiền cước <= 0
    df_cleaned = data[(data['passenger_count'] > 0) & (data['total_amount'] > 0)]
    
    # Chuyển đổi định dạng thời gian
    df_cleaned['tpep_pickup_datetime'] = pd.to_datetime(df_cleaned['tpep_pickup_datetime'])
    
    return df_cleaned