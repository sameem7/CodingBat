# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
# Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

# Ex: make_chocolate(4, 1, 9) → 4
#     make_chocolate(4, 1, 10) → -1
#     make_chocolate(4, 1, 7) → 2

def make_chocolate(small, big, goal):
  
  # If the total available amount of chocolate is less than the goal or if goal%5 is greater than the number of avialable small bars,
  # the combination cannot be made successfully
  if (big*5+small<goal or goal%5>small):
    return -1
  
  # If total number of big bars is greater than or equal to the goal,
  # we would require goal%5 number of small bars
  elif(big*5 >= goal):
    return goal%5
  
  # Otherwise the number of small bars required is the difference between the goal and the total of big bars
  else:
    return (goal-big*5)
