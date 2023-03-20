import pandas as pd
import os
from env import user, host,password
def get_connection(schema,
                   user=user,
                   host=host,
                   password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{schema}'
def telco_data():
    if os.path.exists('telco_churn.csv'):
        df = pd.read_csv('telco_churn.csv',index_col=0)
    else:
        query = 'select * from customers'
        connection = get_connection('telco_churn')
        df=pd.read_sql(query,connection)
    return df