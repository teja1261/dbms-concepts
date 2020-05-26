Q1 = '''SELECT d.id, d.fname FROM Director AS d WHERE EXISTS (SELECT * FROM MovieDirector INNER JOIN Movie on id = mid WHERE year > 2000 AND d.id = MovieDirector.did) AND NOT EXISTS (SELECT * FROM MovieDirector INNER JOIN Movie on id = mid WHERE year < 2000 AND d.id = MovieDirector.did) ORDER BY d.id ASC;'''

Q2 = '''SELECT fname, (SELECT name FROM Movie INNER JOIN MovieDirector on id = MovieDirector.mid WHERE did = d.id ORDER BY rank DESC,name ASC LIMIT 1) FROM Director AS d LIMIT 100;'''

Q3 = '''SELECT * FROM Actor WHERE NOT EXISTS (SELECT * FROM Cast INNER JOIN Movie on id = mid AND `Actor`.`id` = pid  WHERE year BETWEEN 1990 AND 2000) ORDER BY `Actor`.`id` DESC LIMIT 100;'''
