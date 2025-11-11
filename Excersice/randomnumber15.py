import random

low=1
high=100
# guesses=0
options=("rock","paper","scissors")
card=["1","2","3","4","5","Q","K","A"]

# number=random.randint(low,high)
number=random.random()
option=random.choice(options)
print(option)

random.shuffle(card)
print(card)