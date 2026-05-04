try:
    def cal():
        global store
        result = 0
        a = int(input("Enter 1st number: "))
        b = int(input("Enter 2nd number: "))
        c = input("Enter an operator: ").strip()
        if c == "+":    
            result = (a + b)

        elif c == "-":
            result = (a - b)

        elif c == "*":
            result = (a * b)

        elif c == "/":
            if b == 0: 
                print("Error: Division by zero\n")
                cal()
            else:    
                result = (a / b)    

        else:
            print("Invalid operator")

        print(result)    
        store = (a,c,b,"=",result)
        ling.append(store)

    def main():
        global ling
        ling = []
        while True:
          cal()
          f = input("Do you want to continue? Yes or No: ").strip().lower()
          if f == "yes":
             continue
          else:
             print(ling)
             break

    main()

except ValueError:
    print("Invalid input. Please enter a valid number.")

