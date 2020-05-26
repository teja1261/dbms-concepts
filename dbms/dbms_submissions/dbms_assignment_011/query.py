Q1 = '''SELECT `Actor`.`id`,fname,lname,gender FROM Actor INNER JOIN Cast on `Cast`.`pid` = `Actor`.`id` INNER JOIN Movie on `Movie`.`id` = `Cast`.`mid` WHERE name LIKE 'Annie%';'''

Q2 = '''SELECT `Movie`.`id`, name, rank, year FROM Movie INNER JOIN MovieDirector on `MovieDirector`.`mid` = `Movie`.`id` INNER JOIN Director on `Director`.`id` = `MovieDirector`.`did` WHERE fname = "Biff" AND lname = "Malibu" AND year IN (1999, 1994, 2003) ORDER BY rank DESC, year ASC;'''

Q3 = '''SELECT year, COUNT(id) AS no_of_movies FROM Movie GROUP BY year HAVING AVG(rank) > (SELECT AVG(rank) FROM Movie) ORDER BY year ASC;'''

Q4 = '''SELECT id, name, year, rank FROM Movie WHERE year = 2001 AND rank < (SELECT AVG(rank) FROM Movie) ORDER BY rank DESC LIMIT 10;'''

Q5 = '''SELECT m.id, (SELECT COUNT(gender) FROM Actor INNER JOIN Cast on `Cast`.`pid` = `Actor`.`id` WHERE m.id = `Cast`.`mid` AND gender = 'F') AS no_of_female_actors, (SELECT COUNT(gender) FROM Actor INNER JOIN Cast on `Cast`.`pid` = `Actor`.`id` WHERE m.id = `Cast`.`mid` AND gender = 'M') AS no_of_male_actors FROM Movie AS m ORDER BY m.id ASC LIMIT 100;'''

Q6 = '''SELECT DISTINCT(pid) FROM Cast INNER JOIN Movie on `Movie`.`id` = `Cast`.`mid` GROUP BY mid,pid HAVING COUNT(DISTINCT(role)) > 1 ORDER BY pid ASC LIMIT 100;'''

Q7 = '''SELECT DISTINCT(fname), COUNT(fname) AS count FROM Director GROUP BY fname HAVING count > 1;'''

Q8 = '''SELECT `D`.`id`, fname, lname FROM Director AS D WHERE EXISTS (SELECT did FROM MovieDirector INNER JOIN Cast on `Cast`.`mid` = `MovieDirector`.`mid` WHERE `D`.`id` = `MovieDirector`.`did` GROUP BY `MovieDirector`.`mid` HAVING COUNT(DISTINCT pid) >= 100) AND NOT EXISTS (SELECT did FROM MovieDirector INNER JOIN Cast on `Cast`.`mid` = `MovieDirector`.`mid` WHERE `D`.`id` = `MovieDirector`.`did` GROUP BY `MovieDirector`.`mid` HAVING COUNT(DISTINCT pid) < 100);'''


#Q5 = '''SELECT m.id, (SELECT COUNT(gender) FROM Actor INNER JOIN Cast on `Cast`.`pid` = `Actor`.`id` WHERE m.id = `Cast`.`mid` AND gender = 'F') AS no_of_female_actors, (SELECT COUNT(gender) FROM Actor INNER JOIN Cast on `Cast`.`pid` = `Actor`.`id` WHERE m.id = `Cast`.`mid` AND gender = 'M') AS no_of_male_actors FROM Movie AS m ORDER BY m.id ASC LIMIT 100;'''