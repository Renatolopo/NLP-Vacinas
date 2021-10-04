import pymysql as MySQLdb
import pandas as pd

class Noticias_DB:
    def __init__(self):
        self.conection = MySQLdb.connect(host='',
                            user='renato',
                            password='',
                            db='Monitor_de_noticia',)

    def get_df(self, name):
        return  pd.read_sql(f'select * from {name};', con=self.conection)
    