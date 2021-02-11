"""
List of student scores on the final exam in a particular order, and you want to reward
your students. You decide to do so fairyly by giving them arbitrary rewards following two rules:
1) all students must receive at least one reward
2) any studen must receive strictly more rewards than an adjacent student with a lower score.
"""


# O(n) Time & O(n) Space
def min_rewards(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        if scores[i] > scores[i-1]:
            rewards[i] = rewards[i-1] + 1
    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i+1]:
            rewards[i] = max(rewards[i], rewards[i+1]+1)
    return sum(rewards)


scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
# 25 would be this result based on [4, 3, 2, 1, 2, 3, 4, 5, 1]
print(min_rewards(scores))
