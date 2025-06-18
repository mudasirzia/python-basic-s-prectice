# 

class calculator:
    # 
    # 
    def __init__(self,n,m):
        # 
        self.n = n
        # self.op = op
        self.m = m

    # add
    def add(self):
        # 
        return self.n + self.m
    
    # subtract
    def sub(self):
        # 
        try:
            
            if self.n > self.m:

                return self.n - self.m
            
            else:

                print("number 2 is greater than 1")

        except ValueError:
            # 
            raise ValueError
    
    #mutiply
    def multiply(self):
        # 
        return self.n * self.m
    
    # divide
    def div(self):
        # 
        try:

            if self.m != 0:

                return self.n / self.m
            
            else:

                print("Can't divide by zero!!!")

        except ZeroDivisionError:
            # 
            raise ZeroDivisionError


# 
if __name__ == "__main__":
    # 
    num1 = int(input("Enter the first number:\t"))
    # 
    num2 = int(input("Enter the second number:\t"))
    # 
    cal = calculator(num1,num2)
    # 
    signs = ["+","-","*","/"]

    for sign in signs:

        try:
            if sign == "+":
                # 
                result = cal.add()

            elif sign == "-":
                # 
                result = cal.sub()

            elif sign == "*":
                # 
                result = cal.multiply()

            elif sign == "/":

                result = cal.div()
            else:

                print("invalid syntex")

        except ValueError:
            # 
            raise ValueError
        # 

        print(f"{num1} {sign} {num2} = {result}")
    
    # 


