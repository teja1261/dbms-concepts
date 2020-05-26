Q1 = '''SELECT pid AS actor_id, COUNT(pid) AS no_of_movies FROM Cast GROUP BY pid;'''

Q2 = '''SELECT year, COUNT(id) FROM Movie GROUP BY year ORDER BY year ASC;'''

Q3 = '''SELECT year, AVG(rank) FROM Movie GROUP BY year HAVING COUNT(Id) >= 10 ORDER BY year DESC;'''

Q4 = '''SELECT year, MAX(rank) AS max_rank FROM Movie GROUP BY year ORDER BY year ASC;'''

Q5 = '''SELECT rank, COUNT(id) AS no_of_movies FROM Movie WHERE name LIKE "a%" GROUP BY rank;'''
