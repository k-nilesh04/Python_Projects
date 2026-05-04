#let's create a periodic table using python

dic = { "H" : { "Name" : "Hydrogen",
               "Group" : "1", 
               "Period" : "1", 
               "Atomic Number" : "1", 
               "Atomic Mass" : "1.008", 
              },
       "He" : { "Name" : "Helium", 
               "Group" : "18", 
               "Period" : "1", 
               "Atomic Number" : "2", 
               "Atomic Mass" : "4.0026", 
              },
       "Li" : { "Name" : "Lithium", 
               "Group" : "1", 
               "Period" : "2", 
               "Atomic Number" : "3", 
               "Atomic Mass" : "6.94", 
              },
       "Be" : { "Name" : "Beryllium", 
               "Group" : "2", 
               "Period" : "2", 
               "Atomic Number" : "4", 
               "Atomic Mass" : "9.0122", 
              },
       "B" : { "Name" : "Boron", 
              "Group" : "13", 
              "Period" : "2", 
              "Atomic Number" : "5", 
              "Atomic Mass" : "10.81", 
             },
       "C" : { "Name" : "Carbon", 
              "Group" : "14", 
              "Period" : "2", 
              "Atomic Number" : "6", 
              "Atomic Mass" : "12.011", 
             },
       "N" : { "Name" : "Nitrogen", 
              "Group" : "15", 
              "Period" : "2", 
              "Atomic Number" : "7", 
              "Atomic Mass" : "14.007", 
             },
       "O" : { "Name" : "Oxygen", 
              "Group" : "16", 
              "Period" : "2", 
              "Atomic Number" : "8", 
              "Atomic Mass" : "15.999", 
             },
       "F" : { "Name" : "Fluorine", 
              "Group" : "17", 
              "Period" : "2", 
              "Atomic Number" : "9", 
              "Atomic Mass" : "18.998", 
             },
       "Ne" : { "Name" : "Neon", 
               "Group" : "18", 
               "Period" : "2", 
               "Atomic Number" : "10", 
               "Atomic Mass" : "20.180", 
              }

      }

print()

def end():
  print()
  print("Here is the Periodic Table:\n\t",dic)


def move5():
  print()
  print("Want to delete an element in this periodic table?:")
  s = input("Enter Yes or No: ")
  if s == "Yes" or s == "yes" or s == "y":
    hi = input("Enter the element Symbol:").capitalize()
    print()
    print(f"Element deleted: {dic.pop(hi)}")
    move5()
  else:
    print()
    print("Thank you for using this periodic table")
    end()


###################################


def move4():
  print("Want to update an element Atomic mass:")
  p = input("Enter Yes or No: ").lower()
  if p == "yes" or p == "y":
    h = input("Enter the element Symbol:").capitalize()
    if h in dic :
      f = input("Enter new atomic mass:")
      dic[h]["Atomic Mass"] = f
      print("Updated Atomic Mass:",dic[h])
      move4()

    else:
      print("Element not found")
      move4()

  else:
    print()
    move5()


##################################3


def move3():
  print("Want to search for an element in this periodic table?:")
  kk = input("Enter Yes or No: ").lower()
  if kk == "yes" or kk == "y":
    g = input("Enter the element Symbol:").capitalize()
    if g in dic :
      print(f"Element found: {dic[g]}")
    else:
      print("Element not found")
      move3()
    print()
    move3()
  else:
    print()
    move4()


####################################


def add_element():
  #add element in dic using input
   a = input("Enter the element Symbol:")
   b = input("Enter the element Name:")
   c = input("Enter the element Group:")
   d = input("Enter the element Period:")
   e = input("Enter the element Atomic Number:")
   f = input("Enter the element Atomic Mass:")
   z = { a : {"Name" : b,
             "Group" : c,
             "Period" : d, 
             "Atomic Number" : e, 
             "Atomic Mass" : f,
            }
      }
   dic.update(z)
   print()
   print("Added element in Periodic table:\n",dic[a])
   print()
   print("Here is the New Periodic Table:\n\t",dic)
   print()
   move2()

def move2():
  print("Want to add a new element in this periodic table?:")
  k = input("Enter Yes or No: ")
  if k == "Yes" or k == "yes" or k == "y":
    add_element()

  else:
    print()
    move3()


###########################


def know_element():
  ak = input("Enter element symbol:").capitalize()
  bk = input("What you want Atomic Number/Atomic Mass/Name/Group/Period:").title()
  if ak in dic and bk in dic[ak]:
    print(dic[ak][bk])
    print()
    move()
  else:
    print("Enter valid element symbol and property")
    move()


def move():
  print("Want to know about an element?:")
  a = input("Enter Yes or No: ").lower()
  if a == "yes" or a =="y":
    know_element()
  else:
    print()
    move2()
move()


