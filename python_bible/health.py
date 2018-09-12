import random

health = 50
dificuilty = 5
health_potion = int(random.randint(25,50) / dificuilty)

health = health + health_potion

print(health)
