matches = [("TeamA", "TeamB", 2, 1), ("TeamC", "TeamA", 0, 3)]
scores = {}
for match in matches:
    winner = match[0] if match[2] > match[3] else match[1]
    scores[winner] = scores.get(winner, 0) + 1
else:
    print("Final scores:", scores)