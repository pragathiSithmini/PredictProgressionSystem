#4COSC006C: Software Development I – Coursework specification (2020/21)
#Part 1 - Student Version


# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1810216        
# Date: 10/12/2020



def predictProgress(credit_pass,credit_defer,credit_fail):   #function for check the progression outcome. 
    if credit_pass==120:
        print("Progress")
    elif credit_pass==100:
        print("Progress (module trailer)")
    elif (credit_fail<=60):
        print("Do not progress – module retriever")
    elif (credit_fail>=80 and credit_fail<=120):
        print("Exclude")
#CODE_______________________________________
        
print( )    
print("___Student Version___")
print( )
credit_pass=int(input("Please enter your credit at pass  : "))   #ask the user for a credit pass
credit_defer=int(input("Please enter your credit at defer: ")) #ask the user for a credit defer
credit_fail=int(input("Please enter your credit  at fail : "))  #ask the user for a credit fail

predictProgress(credit_pass,credit_defer,credit_fail) # call for the predictprogress function that defined above.
