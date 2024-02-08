import pandas as pd


def excel_to_dict(file_name, sheet_name):
    data_frame = pd.read_excel(file_name, sheet_name)
    data_dict = data_frame.to_dict(orient='records')
    return data_dict
