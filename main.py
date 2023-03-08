import pandas as pd
import pymysql
from sqlalchemy import create_engine
import configparser

import time
from argparse import ArgumentParser

from data import loading
import settings

parser = ArgumentParser()

parser.add_argument("-a","--atype",type=str)
parser.add_argument("-fp","--file_path",type=str)
parser.add_argument("-tn","--table_name",type=str)

args = parser.parse_args()

if __name__ == "__main__":

    FLAGS = args
    atype = FLAGS.atype if FLAGS.atype else "csv"
    file_path = FLAGS.file_path if FLAGS.file_path else "./data/"
    table_name = FLAGS.file_path if FLAGS.table_name else "gender"

    # check time
    start_time = time.time()

    # load data set
    df = loading(atype, file_path, table_name)

    # create engine
    path = f"mysql+pymysql://{settings.user}:{settings.password}@{settings.host}:{settings.port}/{settings.DB}"
    engine = create_engine(path)

    # upload data

    df.to_sql(index=False, name=table_name, con=engine, if_exists='replace')

    print("걸린 시간: ",round((time.time()-start_time)/60,4),"min")
    print("MySQL DB 적재 완료")