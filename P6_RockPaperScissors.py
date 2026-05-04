import random

print("Welcome to Rock, Paper, Scissors!\n \n 1 = Rock\n 2 = Paper\n 3 = Scissors\n ")

pp = [ ]
i = 0
while i < 5:
  comp = random.randint(1, 3)
  user  = int(input("Enter your choice: "))

  def  rps(comp, user):
      if user  == comp :
        print(f"\nComputer chose {comp} and you chose {user}.")
        print("It's a tie!")

        return 0

      elif ( user  == 1 and comp == 3 ) or (user  == 2 and comp == 1) or  (user  == 3 and comp == 2) :
         print(f"\nComputer chose {comp} and you chose {user}.")
         print("You win!")
         return 1

      elif (user  == 1 and comp == 2)  or (user  == 2 and comp == 3) or (user  == 3 and comp == 1):
         print(f"\nComputer chose {comp} and you chose {user}.")
         print("You lose!")
         return -1


  def score(comp, user):
    pp.append(rps(comp, user))
    print(f"Your score is {pp}\n")


  score(comp,user)
  i += 1

print(f" Total sum of score = {sum(pp)}")