# src/database/tables.py

import peewee as pw

db = pw.SqliteDatabase("src/database/database.db")

class BaseModel(pw.Model):
    class Meta:
        database = db

class Introduction(BaseModel):
    '''
    user_id: int : primary key
    part: int
    introduction: str

    part ::
    0 - Name
    1 - Birth Date
    2 - Reason for joining
    3 - Political Views
    '''
    user_id = pw.IntegerField(unique=True, primary_key=True)
    part = pw.IntegerField()
    introduction = pw.TextField()