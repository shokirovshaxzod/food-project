#Небольшая игра на угадывание
import random
Secret = "Я задумал число от 1 до 1000"
Case = random.randint(1,1000)
print(Case)
print(Secret)
print("Угадай число: ", end="")
Input = 0
while Input != Case :
  print("Угадай число: ", end="")
  Input = int(input())
  if Input < Case :
    print("Слишком маленькое!")
  if Input > Case :
    print("Слишком большое!")
  if Input == Case :
    print("Правильно!")
if Input < Case :
  print("Слишком маленькое!")
if Input > Case :
  print("Слишком большое!")
if Input == Case :
  print("Правильно!")

