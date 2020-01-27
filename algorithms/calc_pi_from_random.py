"""
Given a function which generate n random float number range from 0 to 1 which is uniformly distributed
Random func can be called multiple times
Calculate the pi
"""
import random
def calc_pi(n):
    inside_count = 0
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if (x**2 + y**2) < 1:
            inside_count += 1
    
    return 4*(inside_count/n)


print(calc_pi(10000))

