Q1 = '''SELECT COUNT(id) FROM Movie WHERE year < 2000;'''

Q2 = '''SELECT AVG(rank) FROM Movie WHERE year = 1991;'''

Q3 = '''SELECT MIN(rank) FROM Movie WHERE year = 1991;'''

Q4 = '''SELECT fname, lname FROM Actor INNER JOIN Cast on id = pid WHERE mid = 27;'''

Q5 = '''SELECT COUNT(id) FROM Actor INNER JOIN Cast on id = pid WHERE (fname = 'Jon' AND lname = 'Dough');'''

Q6 = '''SELECT name FROM Movie WHERE (year BETWEEN 2003 AND 2006) AND name LIKE 'Young Latin Girls%';'''

Q7 = '''SELECT fname, lname FROM MovieDirector INNER JOIN Director on did = Director.id INNER JOIN Movie on Movie.id = mid WHERE name LIKE "Star Trek%";'''

Q8 = '''SELECT name FROM MovieDirector INNER JOIN Director on `Director`.`id` = `MovieDirector`.`did` INNER JOIN Movie on `Movie`.`id` = `MovieDirector`.`mid` INNER JOIN Cast on `Movie`.`id` = `Cast`.`mid` INNER JOIN Actor on `Actor`.`id` = `Cast`.`pid` WHERE (Actor.fname = "Jackie (I)" AND Director.fname = "Jackie (I)") AND (Actor.lname = "Chan" AND Director.lname = "Chan") ORDER BY name ASC;'''

Q9 = '''SELECT fname,lname FROM Director INNER JOIN MovieDIRECTOR ON `Director`.`id` = did INNER JOIN Movie ON `Movie`.`id` = mid WHERE year = 2001 GROUP BY did HAVING COUNT(mid)>=4 ORDER BY fname ASC,lname DESC;'''

Q10 = '''SELECT gender, COUNT(gender) FROM Actor GROUP BY gender ORDER BY gender ASC;'''

Q11 = '''SELECT DISTINCT `m1`.`name`, `m2`.`name`, `m1`.`rank`, `m1`.`year` FROM Movie AS m1, Movie AS m2 WHERE (`m1`.`rank` = `m2`.`rank` AND `m1`.`year` = `m2`.`year`) AND `m1`.`name` <> `m2`.`name` ORDER BY `m1`.`name` ASC LIMIT 100;'''

Q12 = '''SELECT fname, year, AVG(rank) FROM Cast INNER JOIN Actor ON `Actor`.id = `Cast`.pid INNER JOIN Movie ON `Movie`.id = `Cast`.mid GROUP BY year, `Actor`.`id` ORDER BY fname ASC, year DESC LIMIT 100;'''

Q13 = '''SELECT `Actor`.`fname`, `Director`.`fname`, AVG(rank) AS score FROM MovieDirector INNER JOIN Director on `Director`.`id` = `MovieDirector`.`did` INNER JOIN Movie on `Movie`.`id` = `MovieDirector`.`mid` INNER JOIN Cast on `Cast`.`mid` = `MovieDirector`.`mid` INNER JOIN Actor on `Actor`.`id` = `Cast`.`pid` GROUP BY `Actor`.`id`, `Director`.`id` HAVING COUNT(`Movie`.`id`) >= 5 ORDER BY score DESC, `Director`.`fname` ASC, `Actor`.`fname` DESC LIMIT 100;'''