#Author:
#Dilpreet Singh Chawla
#Indian Institute of Information Technology Kalyani.

#Newton's Method to find square root of a positive number
def square_root(n):
    if n<0:
        raise RuntimeError("Please enter a positive number!")
    else:
        root=n/2 #initial_guess
        for k in range(20):
            root=(1/2)*(root+n/root) #new_guess = 1/2 * (old_guess + n / old_guess)
            
        return root

#To take input from user
n=float(input("Enter a number: "))

#Calling Function
sqrt=square_root(n)

#Printing the result
print("The square root of the number is : ",sqrt)
