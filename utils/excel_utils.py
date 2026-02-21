import random

import pandas as pd


def read_data(relativepath,sheetname):
    data=pd.read_excel(relativepath,sheetname)
    return data.to_dict(orient="records")



def randomize_record(excel,sheetname,column_name):
    data = read_data(excel, sheetname)[0][column_name]

    randomnum=random.randint(1,100)
    record=f"{data}_{randomnum}"

    return record






