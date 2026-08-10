Interview Hint

Whenever you hear:

Consecutive
Continuous
Longest streak
Maximum consecutive

Think:
"Do I need to compare elements?"

Usually No.

Instead ask:
"Can I maintain a running count?"
If yes, that's almost always the simpler and optimal solution.

Interview Tip

Whenever a question contains words like:

Longest consecutive
Continuous
Streak
Maximum consecutive

think of this pattern:

count = 0
maximum = 0

for element in array:

    if condition:
        count += 1
        maximum = max(maximum, count)
    else:
        count = 0