#4COSC006C: Software Development I – Coursework specification (2020/21)
#Part 2 – Student Version (Validation)

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1810216        
# Date: 10/12/2020

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def getCreditValue(input_message):                   # get user input. validation logics are same for every input
  while True:                                        # function for get input message and check the validtion and also that is an integer.
    try:
      value = int(input(input_message))             
      if value in [0, 20, 40, 60, 80, 100, 120]:    #check validation for every part.
        return value
      else:
        print("Out of range.")
    except:
      print("Integer required.")                      #if input isn't an integer,printing the integer as required.




def predictProgress(credit_pass,credit_defer,credit_fail):    #function for check the progression outcome.
    if credit_pass==120:
        print("Progress")
    elif credit_pass==100:
        print("Progress (module trailer)")
    elif (credit_fail<=60):
        print("Do not progress – module retriever")
    elif (credit_fail>=80 and credit_fail<=120):
        print("Exclude")


        
def check():                                                #function for check the defined function called as getCreditValue(input_message) and also check the total.
  while True:
     credit_pass= getCreditValue("Please enter your credits at pass : ")
     credit_defer= getCreditValue("Please enter your credit at defer : ")  #In this execute the getCreditValue(input_message) function.
     credit_fail = getCreditValue("Please enter your credit at fail : ")
     if credit_pass +credit_defer+ credit_fail == 120:                     #In this check the total and when total is equal to 120,programme will be break.And also catch the value which returned from getCreditValue(input_message) function.
       break
     else:
      print("Total incorrect.")
  predictProgress(credit_pass,credit_defer,credit_fail)                    #In this case execute the predictProgress function for check the progression outcome which generated above.


#CODE________________________________________________________________________________________________________________________________________________________________________________

print( )                                                     
print("___Student Version (Validation)___")
print( )
check()                                                         #This is the final code and executes the function called check() which defined above.



