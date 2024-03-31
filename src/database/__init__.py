import peewee as pw
from . import tables

import logging

logger = logging.getLogger("cyan")

db = pw.SqliteDatabase("src/database/database.db")

def create_tables():
    db.connect()
    db.create_tables([tables.Introduction])
    logger.debug("Tables created.")
    db.close()

def drop_tables():
    db.connect()
    db.drop_tables([tables.Introduction])
    logger.debug("Tables dropped.")
    db.close()

def reset_tables():
    drop_tables()
    create_tables()
    db.close()

def reset_table(table : tables.BaseModel):
    db.connect()
    db.drop_tables([table])
    db.create_tables([table])
    logger.debug(f"Table {table} reset.")
    db.close()
