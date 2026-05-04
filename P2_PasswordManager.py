#Let's Create a password manager using python

dict = {}
def save_password():
  a = input("Enter the Title of the password: ").strip()
  b = input("Enter the password: ").strip()
  z = {a:b}
  dict.update(z)
  print(f"Password saved successfully with Title {a}")
  print()

def retrieve_password():
  c = input("Enter the Title of the password: ").strip()
  if c in dict:
    print(f"Password for {c} is {dict[c]}")
  else:
    print("Password not found or wrong Title entered")
  print()  

def update_password():
  d = input("Enter the Title for which you want to update the password: ").strip()
  if d in dict:
    e = input("Enter the new password: ").strip()
    dict[d] = e
    print(f"Password for {d} updated successfully")
    print()
  else:
    print("Password not found or wrong Title entered")
  print()

def delete_password():
  f = input("Enter the Title for which you want to delete the password: ").strip()
  if f in dict:
    dict.pop(f)
    print(f"Password for {f} deleted successfully")
  else:
    print("Password not found or wrong Title entered")
  print()  

def show_passwords():
  if dict == {}:
    print("No passwords saved")
  else:
    print("Here are all the passwors saved:")
    for i in dict:
      print(f"Title: {i} Password: {dict[i]}  ")

def main():

  k = input("Enter the number of your choice: ").strip()

  if k == "1":
    save_password()
    print()
    main()
  elif k == "2":
    retrieve_password()
    print()
    main()
  elif k == "3":
    update_password()
    print()
    main()
  elif k == "4":
    delete_password()
    print()
    main()
  elif k == "5":
    show_passwords()
    print()
    main()
  elif k == "6":
    print()
    print()
    print("Thank you for using the password manager")
  else:
    print("Invalid choice")
    print()
    main()


print("Welcome to the password manager")
print("Choose an option:")
print( "1. Want to save a password \n2. Want to see a Specific password \n3. Want to update a password \n4. Want to delete a password \n5. Want to see all saved passwords \n6. Want to exit the program" )
print()
main()
