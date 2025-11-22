import sqlite3
import os
from automation_framework.core.logger import setup_logger

logger = setup_logger()

class DBClient:
    def __init__(self, db_name="test_db.sqlite"):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        logger.info(f"Connected to database: {self.db_name}")

    def close(self):
        if self.conn:
            self.conn.close()
            logger.info("Closed database connection")

    def execute_script(self, script_path):
        with open(script_path, 'r') as f:
            script = f.read()
        self.conn.executescript(script)
        logger.info(f"Executed script: {script_path}")

    def execute_query(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor

    def fetch_all(self, query, params=()):
        cursor = self.execute_query(query, params)
        return cursor.fetchall()
