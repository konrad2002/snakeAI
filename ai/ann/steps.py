# steps for special situations

import pymysql

class Steps (object):
    def __init__(self):

        self.db = pymysql.connect(
            host = "host",
            user = "usr",
            passwd = "pw",
            database = "db"
        )

        self.cursor = self.db.cursor()

    def saveSteps(self):

        j = 0
        m = 4 * 32 * 24

        for i in range(4):
            
            for a in range(24):
                for b in range(32):

                    j += 1

                    if j % 30 == 0:
                        print( str( round( ( j / m ) * 100 ) ) + "%" )

                    x1 = [a, b, 23 - a, 31 - b]

                    if i == 0:
                        x2 = [1, 0, 0, 0]
                        y = 0

                    if i == 1:
                        x2 = [0, 1, 0, 0]
                        y = 1

                    if i == 2:
                        x2 = [0, 0, 1, 0]
                        y = 2

                    if i == 3:
                        x2 = [0, 0, 0, 1]
                        y = 3

                    query = "INSERT INTO feature_steps (inputs, direction) VALUES (\"" + str([x1, x2, [0, 0, 0, 0]]) + "\", \"" + str(y) + "\")"

                    self.cursor.execute(query)
                    self.db.commit()



steps = Steps()
steps.saveSteps()

