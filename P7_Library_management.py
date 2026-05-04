class Library():
  def __init__(self, bookname, quantity):
     self.bookname = bookname
     self.quantity = quantity

  def book1( self ):
    print(f"Book name is {self.bookname} , quantity is {self.quantity}")

    def hi():      
       print()
       print("Do you want to buy or return the book?")
       print("Enter 1 for Buy")
       print("Enter 2 for Return")
       print()

    if self.quantity > 0:
       print("\nBook is available in the library")
       hi()
       c = int(input("Enter your choice: "))
       if c == 1:
          B_buy = 1
       elif c == 2:
          B_return = 2  
       else:
          print("Invalid choice")

    else:
       print("\nBook is not available in the library")
       hi()
       c = int(input("Enter your choice: "))
       if c == 2:
          B_return == 2  
       else:
          print("Invalid choice")


    if self.quantity > 0 and B_buy == 1 :
       print("Book is bought successfully")
       self.quantity = self.quantity - 1
       no_books[book_list.index(self.bookname)] -= 1

    elif B_return == 2 :
       print("Book is returned successfully")
       self.quantity = self.quantity + 1
       no_books[book_list.index(self.bookname)] += 1
    else:
       print("Byeeee!")


book_list = [ "Python", "Java", "C++", "C", "C#", "JavaScript", "PHP", "Ruby", "Swift",]
no_books = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def main():
    print("Welcome to the Library")
    print()
    def call():
        for i in range(len(book_list)):
            print(f"{i+1}. {book_list[i]} - {no_books[i]}")
    call()       
    print()
    e = input("Enter the book name: ").lstrip()
    if e not in book_list:
       print("Book not found")
       return main()
    else:   
       d = no_books[book_list.index(e)]
       print()
       a = Library(e, d)
       a.book1()
       print()
       call()
main()

while True :
 k = input("Do you want to continue? (yes/no): ").lower()
 if k == "yes":
    main()
 else:
    print("Thank you for using the Library") 
    break
