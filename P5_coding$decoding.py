import random


def randommm():
  k = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",]
  l = ""
  for i in range(3):
    l += random.choice(k)
  bk = (l)  
  return bk


#----------------------------coding--------------------------

def coding():
  a = input("Enter the string: ").strip()
  # global b
  if len(a)>= 3:
    a  = a[1:] + a[0]
    a = a[::-1]
    b = randommm() + a + randommm()
    print("Your coded string is: ",b)

  else:
     print(a[::-1])

#----------------------------decoding-----------------------
def decoding():
  a = input("Enter the string: ").strip()
  if len(a)>= 3:
    a = a[3:-3] 
    a = a[::-1]
    a = a[-1] + a[:-1]
    print(a)

while True:

  print("Enter 1 for coding\nEnter 2 for decoding\nEnter 3 for exit ")
  print()
  option = input("Enter Option:  ")
  print()
  if option  == "1":
    coding()
    print()

  elif option == "2":
    decoding()
    print()

  else:
     break







# we can seperate very element and append something then join...

#other ways of encription also there....