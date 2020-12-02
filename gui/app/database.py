# connection to database (set cursor)

import pymysql

class Database (object):
    def __init__(self):
        
        self.db = pymysql.connect(
            host = "logilutions.de",
            user = "snakeai_public",
            passwd = "moE8kyFvQcz5BYUj",
            database = "snake_public"
        )

        self.cursor = self.db.cursor()