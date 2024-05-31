#4COSC006C: Software Development I – Coursework specification (2020/21)
#Part 4 - Vertical Histogram (optional extension)

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1810216       
# Date: 10/12/2020


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def getCreditValue(input_message):                   # get user input. validation logics are same for every input
  while True:                                        # function for get input message and check the validtion and also that is an integer.
    try:
      value = int(input(input_message))
      if value in [0, 20, 40, 60, 80, 100, 120]:      #check validation for every part.
        return value
      else:
        print("Out of range.")
    except:
      print("Integer required")                      #if input isn't an integer,printing the integer as required.

def predictProgress(credit_pass,credit_defer,credit_fail):     #function for check the progression outcome. 
    if credit_pass==120:
        print("Progress")
        return "Progress"
    elif credit_pass==100:
        print("Progress (module trailer)")
        return "Progress (module trailer)"
    elif (credit_fail<=60):
        print("Do not progress – module retriever")
        return "Do not progress – module retriever"
    elif (credit_fail>=80 and credit_fail<=120):
        print("Exclude")
        return "Exclude"
    
def check():                                                                 #function for check the defined function called as getCreditValue(input_message) and also check the total.                                                      
  while True:
     credit_pass= getCreditValue("Please enter your credits at pass : ")
     credit_defer= getCreditValue("Please enter your credit at defer : ")    #In this execute the getCreditValue(input_message) function.
     credit_fail = getCreditValue("Please enter your credit at fail : ")
     if credit_pass +credit_defer+ credit_fail == 120:                       #In this check the total and when total is equal to 120,programme will be break.And also catch the value which returned from getCreditValue(input_message) function.
       break
     else:
      print("Total incorrect.")
  prediction=predictProgress(credit_pass,credit_defer,credit_fail)           #In this case execute the predictProgress function for check the progression outcome which generated above.
  return  prediction




def increase(prediction):                                                     #function for count the progession outcomes and also catch the prediction which returned from check() funtion
    global no_progress
    global no_trailer                                                         # Global variables are created to store values that increse when the code is running.
    global no_retriever
    global no_Exclude
    if prediction=="Progress":
        no_progress+=1
    elif prediction=="Progress (module trailer)":
        no_trailer+=1
    elif prediction=="Do not progress – module retriever":
        no_retriever+=1
    else:
        no_Exclude+=1
        
        



#CODE___________________________
print( )
print("---Staff Version with Histogram---")
print( )
no_progress=0
no_trailer=0
no_retriever=0
no_Exclude=0

prediction=check()                                                                  #Executes check function and assigns prediction for variable called prediction.
increase(prediction)                                                                #After that executes the increase function.This is  being done beacuse before asking the choice, programme must be execute one time.
while True:
    print( )
    choice=input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results : ")             #ask the choice from the user.
    choice=choice.lower()
    if choice=="y":
        prediction=check()                                                                                                          #Executes check function and assigns prediction for variable called prediction.
        increase(prediction)                                                                                                        #Execute the increase function.
        continue
    elif choice=="q":
        print( )
        print("-----------------------------------------------------------------------------------")
        print("___HORIZONTAL HISTOGRAM___")
        print( )
        print('Progress ',no_progress,':',"*"*no_progress)
        print('Trailer  ',no_trailer,':',"*"*no_trailer)
        print('Retriever',no_retriever,':',"*"*no_retriever)                                                                     #Display Horizontal Histogram.
        print('Exclude  ',no_Exclude,':',"*"*no_Exclude)
        no_of_all_outcomes=no_progress+no_trailer+no_retriever+no_Exclude
        print( )
        print(no_of_all_outcomes,"outcomes in total.")
        print("-----------------------------------------------------------------------------------")
        print( )
        print("___VERTICAL HISTOGRAM___")
        print( )
        print("Progress",no_progress, "Trailer",no_trailer, "Retriever",no_retriever, "Excluded",no_Exclude )                                                                       #Display vertical histogram
        for x in range (max(no_progress,no_trailer,no_retriever,no_Exclude)):
          if x<no_progress:
            print("   *   ",end="   ")
          else:
            print("       ",end="   ")
          if x<no_trailer:
            print("   *   ",end="   ")
          else:
            print("       ",end="   ")
          if x<no_retriever:
            print("   *   ",end="   ")
          else:
            print("       ",end="   ")
          if x<no_Exclude:
            print("   *   ",end="   ")
          else:
            print("       ",end="   ")
          print("")
        print("-----------------------------------------------------------------------------------")

          
        break
    else:
        print("Invalid Character")
        continue



