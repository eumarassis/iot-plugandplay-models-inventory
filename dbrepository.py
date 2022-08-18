from importlib.resources import contents
import sqlite3

class DbRepository ():
    """Wrapper for SQLite"""

    def __init__(self, db):

        self.conn = sqlite3.connect(db)

        self.cursor = self.conn.cursor()

        self.cursor.execute('create table if not exists Model (id, type, context, displayname,  description)')

        self.cursor.execute('create table if not exists ModelCapability (model_id, type, name, displayname, schema)')
        
        self.conn.commit()

                
    def write_model (self, model_dict):

        contents = model_dict.pop("contents")

        self.cursor.execute("insert into Model values (:id, :type, :context, :displayname,  :description)", model_dict)

        self.cursor.executemany("insert into ModelCapability values (:model_id, :type, :name, :displayname, :schema)", contents)

        self.conn.commit()


    def __del__(self):
        self.conn.close()
