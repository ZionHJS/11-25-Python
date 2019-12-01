import random
def randInt(min=0, max=100):
    num = random.random()*max + min
    return num
print(randInt(0,3))
print(randInt())
print(randInt(min=1, max=300))
print(randInt(min=50, max=100))

