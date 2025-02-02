def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    return goal in (s + s)

s = "abcde"
goal = "cdeab"
print(rotateString(s, goal))

s = "abcde"
goal = "abced"
print(rotateString(s, goal))
