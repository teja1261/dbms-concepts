Q1 = '''SELECT AVG(age) FROM Player;'''

Q2 = '''SELECT match_no, play_date FROM Match WHERE audience > 50000 ORDER BY match_no ASC;'''

Q3 = '''SELECT team_id, COUNT(win_lose) AS Win FROM MatchTeamDetails WHERE win_lose = "W" GROUP BY team_id ORDER BY Win DESC, team_id ASC;'''

Q4 = '''SELECT match_no, play_date FROM Match WHERE stop1_sec > (SELECT AVG(stop1_sec) FROM Match) ORDER BY match_no DESC, play_date DESC;'''

Q5 = '''SELECT `Match`.`match_no`, `Team`.`name`, `Player`.`name` FROM MatchCaptain INNER JOIN Team on `MatchCaptain`.`team_id` = `Team`.`team_id` INNER JOIN Match on `MatchCaptain`.`match_no` = `Match`.`match_no` INNER JOIN Player on `MatchCaptain`.`captain` = `Player`.`player_id` ORDER BY `Match`.`match_no` ASC, `Team`.`name` ASC;'''

Q6 = '''SELECT match_no, `Player`.`name`, jersey_no From Match INNER JOIN Player on `Player`.`player_id` = `Match`.`player_of_match` ORDER BY match_no ASC;'''

Q7 = '''SELECT `Team`.`name` ,AVG(`Player`.`age`) AS avg_age FROM Player INNER JOIN Team on `Player`.`team_id` = `Team`.`team_id` GROUP BY `Team`.`name` HAVING AVG(`Player`.`age`) > 26 ORDER BY `Team`.`name` ASC;'''

Q8 = '''SELECT `Player`.`name`, `Player`.`jersey_no`, `Player`.`age`, COUNT(`GoalDetails`.`player_id`) AS no_of_goals FROM GoalDetails INNER JOIN Player on `Player`.`player_id` = `GoalDetails`.`player_id` GROUP BY `Player`.`player_id` HAVING `Player`.`age` <= 27 ORDER BY no_of_goals DESC,`Player`.`name` ASC;'''

Q9 = '''SELECT team_id, (COUNT(goal_id) * 100.0) / (SELECT COUNT(goal_id) FROM GoalDetails) AS percentage_of_goals FROM GoalDetails GROUP BY team_id;'''

Q10 = '''SELECT AVG(goal_count) FROM (SELECT COUNT(goal_id) AS goal_count FROM GoalDetails INNER JOIN Team on `Team`.`team_id` = `GoalDetails`.`team_id` GROUP BY `Team`.`team_id`);'''

Q11 = '''SELECT player_id, name, date_of_birth FROM Player AS p WHERE NOT EXISTS (SELECT player_id FROM GoalDetails WHERE p.player_id = `GoalDetails`.`player_id`) ORDER BY p.player_id ASC;'''

Q12 = '''SELECT `Team`.`name`, `Match`.`match_no`, audience, audience - (SELECT AVG(audience) FROM Match INNER JOIN MatchTeamDetails mtd on `Match`.`match_no` = `mtd`.`match_no` WHERE mtd.team_id = `MatchTeamDetails`.`team_id`) AS difference_audience FROM Match INNER JOIN MatchTeamDetails on `Match`.`match_no` = `MatchTeamDetails`.`match_no` INNER JOIN Team on `Team`.`team_id` = `MatchTeamDetails`.`team_id` ORDER BY `Match`.`match_no` ASC;'''
