Q1 = '''SELECT Player.player_id, MatchCaptain.team_id,jersey_no,name,date_of_birth,age FROM MatchCaptain INNER JOIN Player on captain = Player.player_id LEFT JOIN GoalDetails on captain = GoalDetails.player_id WHERE goal_id is NULL;'''

Q2 = '''SELECT team_id, COUNT(Match.match_no) AS no_of_games FROM Match INNER JOIN MatchTeamDetails on MatchTeamDetails.match_no = Match.match_no GROUP BY team_id;'''

Q3 = '''SELECT team_id, (SELECT COUNT(goal_id) FROM GoalDetails WHERE GoalDetails.team_id = T.team_id) / cast((SELECT COUNT(player_id) FROM Player WHERE Player.team_id = T.team_id) AS Float) AS avg_goal_score FROM Team AS T WHERE avg_goal_score > 0;'''

Q4 = '''SELECT captain, COUNT(captain) AS no_of_times_captain FROM MatchCaptain INNER JOIN Player on Player.player_id = MatchCaptain.captain GROUP BY captain;'''

Q5 = '''SELECT COUNT(DISTINCT(captain)) AS no_players FROM MatchCaptain INNER JOIN Match on Match.player_of_match = MatchCaptain.captain AND Match.match_no = MatchCaptain.match_no;'''

Q6 = '''SELECT DISTINCT(captain) FROM MatchCaptain AS MC WHERE NOT EXISTS (SELECT MC.captain FROM Match WHERE MC.captain = Match.player_of_match);'''

Q7 = '''SELECT strftime('%m',play_date) AS month, COUNT(match_no) AS no_of_matches FROM Match GROUP BY month ORDER BY no_of_matches DESC;'''

Q8 = '''SELECT jersey_no, COUNT(captain) AS no_captains FROM MatchCaptain INNER JOIN Player on Player.player_id = MatchCaptain.captain GROUP BY jersey_no ORDER BY no_captains DESC, jersey_no DESC;'''

Q9 = '''SELECT player_id, AVG(audience) AS avg_audience FROM Match INNER JOIN MatchTeamDetails on MatchTeamDetails.match_no = Match.match_no INNER JOIN Player on Player.team_id = MatchTeamDetails.team_id GROUP BY player_id ORDER BY avg_audience DESC, player_id DESC;'''

Q10 = '''SELECT team_id, AVG(age) FROM Player GROUP BY team_id;'''

Q11 = '''SELECT AVG(age) AS avg_age_of_captains FROM MatchCaptain INNER JOIN Player on Player.player_id = MatchCaptain.captain;'''

Q12 = '''SELECT strftime('%m',date_of_birth) AS month, COUNT(player_id) AS no_of_players FROM Player GROUP BY month ORDER BY no_of_players DESC, month DESC;'''

Q13 = '''SELECT captain, COUNT(MatchCaptain.match_no) AS no_of_wins FROM MatchTeamDetails INNER JOIN MatchCaptain on MatchTeamDetails.team_id = MatchCaptain.team_id AND MatchTeamDetails.match_no = MatchCaptain.match_no WHERE win_lose = 'W' GROUP BY captain ORDER BY no_of_wins DESC;'''
