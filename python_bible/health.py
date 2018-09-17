import random

health = 50
dificuilty = 10
health_potion = int(random.randint(25,50) / dificuilty)

health = health + health_potion

print(health)
