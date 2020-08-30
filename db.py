import sqlite3

db = sqlite3.connect("snake.db")
db.close()

db = sqlite3.connect("file:snake.db?mode=rwc", uri=True)
cursor = db.cursor()
# sql_command = """
#     CREATE TABLE highscores (
#         id INT PRIMARY KEY,
#         playerType INT,
#         highscore INT
#     )
# """  

sql_command = """
    INSERT INTO highscores (playerType, highscore) VALUES (6, 0)
"""  

# sql_command = """
#     ALTER TABLE 'highscores' MODIFY playerType INT
# """  

# sql_command = "DELETE FROM trainingExamples WHERE aiSensor_0_0 = 0 or aiSensor_1_0 = 0 or aiSensor_2_0 = 0 or aiSensor_3_0 = 0"
cursor.execute(sql_command)
# rows = cursor.fetchall()
# for row in rows:
#     print(row[14])
db.commit()
db.close()