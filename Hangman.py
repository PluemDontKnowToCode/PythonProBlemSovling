#hangman
coub = 0
import random
c = ['hello','hi','google','doctor']

i = random.randrange(len(c))
Guess = ["_"]*len(c[i])
print("".join(Guess))
Target = c[i]

while(Target != ("".join(Guess))):
  cou = 0
  inp = str(input("type one lower charactor a - z "))
  for a in range(len(Guess)):
    if ((inp in Target[a]) & (inp not in Guess[a])):
      Guess[a] = inp
      cou += 1
    
  if (cou == 0):
    print("error")
    coub +=1
  if (coub == 6):
    print("You Dead")
    break
  print("".join(Guess))
  Guess = Guess
  if((Target == ("".join(Guess)))):
    print("Congratulation You win")
    print(c[i])
