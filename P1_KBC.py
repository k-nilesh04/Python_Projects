# let's create  KBC

create = input("Do you want to play KBC? : ")
if create == "yes" or create == "YES" or create == "Yes" :
  print("Let's play")
  print("Here is your first question")
  print("What is the capital of India?")
  print("1. Delhi")
  print("2. Mumbai")
  print("3. Kolakat")
  print("4. Agra")
  ans = input("Enter your Answer: ")
  if ans == "1" or ans == "Delhi" or ans == "delhi" or ans == "DELHI" :
    x = "1"
    print(x)


  print("Here is your Second question")
  print("What is the capital of India?")
  print("1. Delhi")
  print("2. Mumbai")
  print("3. Kolakat")
  print("4. Agra")
  ans = input("Enter your Answer: ")
  if ans == "1" or ans == "Delhi" or ans == "delhi" or ans == "DELHI" :

    y = "1"
    print(y)


  print("Here is your Thired question")
  print("What is the capital of India?")
  print("1. Delhi")
  print("2. Mumbai")
  print("3. Kolakat")
  print("4. Agra")
  ans = input("Enter your Answer: ")
  if ans == "1" or ans == "Delhi" or ans == "delhi" or ans == "DELHI" :
    z = "1"
    print(z)


  print("Here is your Fourth question")
  print("What is the capital of India?")
  print("1. Delhi")
  print("2. Mumbai")
  print("3. Kolakat")
  print("4. Agra")
  ans = input("Enter your Answer: ")
  if ans == "1" or ans == "Delhi" or ans == "delhi" or ans == "DELHI" :
    j = "1"
    print(j)


  print("Here is your Fift question")
  print("What is the capital of India?")
  print("1. Delhi")
  print("2. Mumbai")
  print("3. Kolakat")
  print("4. Agra")
  ans = input("Enter your Answer: ")
  if ans == "1" or ans == "Delhi" or ans == "delhi" or ans == "DELHI" :
    k = "1"
    print(k)


  print("You reached the End")
  l = (x,y,z,j,k)
  sum =0
  for i in l:
    sum = sum + int(i)
  print("Your score:",sum)

else:
  print("Byee")




#unfinished game