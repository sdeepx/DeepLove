import random as r
import math


def love_algo(you, lover):
    len1 = len(you)
    len2 = len(lover)
    per = r.randint(80, 90)
    per2 = r.randint(80, 100)
    per3 = r.randint(30, 60)
    per4 = r.randint(2, 4)
    percentage = ((len1 + per2 / per4) / (len2 + per3))*per
    if percentage > 100:
        love_per = percentage - 100
        pure_love = 100 - love_per
        ceil = math.ceil(pure_love)
        return ceil
    percentage_math = math.ceil(percentage)
    return percentage_math
