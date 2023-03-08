import pandas as pd

# __all__=["loading"]

# def load_csv(file_path, table_name) -> pd.DataFrame:
#     return pd.read_csv(file_path+table_name+".csv")

# def load_json(file_path, table_name) -> pd.DataFrame:
#     return pd.read_json(file_path+table_name+".json")

# def load_excel(file_path, table_name) -> pd.DataFrame:
#     return pd.read_xml(file_path+table_name+".xsl") 

def loading(atype:str, file_path:str, table_name:str) -> pd.DataFrame:
    try:
        if atype == 'csv':
            return pd.read_csv(file_path+table_name+".csv")
        elif atype == 'json':
            return pd.read_json(file_path+table_name+".json")
        elif atype == 'excel':
            return pd.read_excel(file_path+table_name+".xlsx") 
    except Exception as e:
        print('Error 발생: ', e)