import sqlite3

db = sqlite3.connect("snake.db")
db.close()

db = sqlite3.connect("file:snake.db?mode=rwc", uri=True)
cursor = db.cursor()
# sql_command = """
#     CREATE TABLE snakes (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         snake_id INT,
#         created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#         player_type INT,
#         highscore INT,
#         best_weights VARCHAR,
#         best_fitness DOUBLE,
#         worst_weights VARCHAR,
#         worst_fitness DOUBLE,
#         fitnesses VARCHAR,
#         scores VARCHAR,
#         generations INT,
#         population INT,
#         iterations INT,
#         eta DOUBLE,
#         epochs INT,
#         batch INT,
#         start_size INT,
#         fitness_function_id INT,
#         activation_functions VARCHAR,
#         output_functions VARCHAR
#     )
# """  

sql_command = """
    INSERT INTO `snakes` (snake_id, player_type, highscore, best_weights, best_fitness, worst_weights, worst_fitness, fitnesses, scores, generations, population, iterations, eta, epochs, batch, start_size, fitness_function_id, activation_functions, output_functions)
    VALUES (111111, 1, 1, "1", 1, "1", 1, "1", "1", 1, 1, 1, 1, 1, 1, 1, "1", "1", "1");
"""  

# sql_command = """
#     ALTER TABLE 'highscores' MODIFY playerType INT
# """  

# sql_command = """
#     DROP TABLE snakes
# """  

# sql_command = "DELETE FROM trainingExamples WHERE aiSensor_0_0 = 0 or aiSensor_1_0 = 0 or aiSensor_2_0 = 0 or aiSensor_3_0 = 0"
cursor.execute(sql_command)
# rows = cursor.fetchall()
# for row in rows:
#     print(row[14])
db.commit()
db.close()