scores = [77,1,108,101,35,60]
highest_score = scores[0]

for i in scores:
    if i > highest_score:
        highest_score = i
print(highest_score)  

total = sum(scores)
print(total) 