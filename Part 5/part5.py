#4COSC006C: Software Development I – Coursework specification (2020/21)
#Part 5 – Alternative Staff Version (optional extension)


# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1810216        
# Date: 10/12/2020


def predictProgress(credit_pass,credit_defer,credit_fail):       #function for check the progression outcome.
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
    

def increase(prediction):                                   #function for count the progession outcomes and also catch the prediction which returned from check() funtion
    global no_progress
    global no_trailer
    global no_retriever                                      # Global variables are created to store values that increse when the code is running.
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
print("___Alternative Staff Version (optional extension)___")
print( )
no_progress=0
no_trailer=0
no_retriever=0
no_Exclude=0

data=[[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]      #Enter data into the list.
for input in data:
    prediction=predictProgress(input[0],input[1],input[2])                                                               #Execute for loop for a sublist inside the list.
    increase(prediction)                                                                                                #Execute the increase function.
    

print("-----------------------------------------------------------------------------------")
print( )
print("---HORIZONTAL HISTOGRAM---")
print( )
print('Progress ',no_progress,':',"*"*no_progress)
print('Trailer  ',no_trailer,':',"*"*no_trailer)
print('Retriever',no_retriever,':',"*"*no_retriever)                                                     #Display Horizontal Histogram.
print('Exclude  ',no_Exclude,':',"*"*no_Exclude)
print( )
no_of_all_outcomes=no_progress+no_trailer+no_retriever+no_Exclude
print(no_of_all_outcomes,"outcomes in total.")
print("-----------------------------------------------------------------------------------")

        
