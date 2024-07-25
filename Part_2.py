# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution
#https://www.w3schools.com/python/python_functions.asp

# IIT Student ID: 20221296
# UoW ID: w1956356
# Date: 07/10/2022

#Makaing def funtion to create list
def students_credits ( message,listname):
    for x in listname:
        print(f'{message} {str(x).replace("[", "").replace("]", "")}')
        
#Making list to collect progression outcome
progress_list       = []
module_trailer_list = []
retriever_list      = []
exclude_list        = []

#counting the progression outcome of the student 
progress       = 0
module_trailer = 0
retriever      = 0
exclude        = 0

#Input credits of the students and check whether is is valid or not !
while True:
    try:
        while True:
            pass_credit = int(input("Enter your total PASS credits : "))
            if pass_credit not in range(0,121,20):
                print("out of range")
                continue
            else:
                break
        while True:    
            defer_credit = int(input("Enter your total DEFER credits: "))
            if defer_credit not in range(0,121,20):
                print("out of range")
                continue
            else:
                break
        while True:
            fail_credit = int(input("Enter your total FAIL credits : "))
            if fail_credit not in range(0,121,20):
                print("out of range")
                continue
            else:
                break
    except ValueError:
         print ("Integer required")
         continue
        
#check the validity of total credit
    total_credit = pass_credit + defer_credit + fail_credit
    if total_credit != 120:
        print("Total incorrect")
        continue
    
#selecting the progress outcome
    if pass_credit == 120:
        print("Progress")
        progress += 1
        progress_list.append([pass_credit , defer_credit , fail_credit])
        
    elif pass_credit == 100:
        print("Progress (module trailer)")
        module_trailer += 1
        module_trailer_list.append([pass_credit,defer_credit,fail_credit])
        
    elif 80 >= pass_credit and 80 > fail_credit:
        print("Do not progress - Module retriever")
        retriever += 1
        retriever_list.append([pass_credit,defer_credit,fail_credit])
        
    elif fail_credit >= 80:
        print("Exclude")
        exclude += 1
        exclude_list.append([pass_credit,defer_credit,fail_credit])
        
#selecting continuation of the progress
    option =str(input("Would you like to enter another set of data ?\nEnter \'y\' for yes or \'q\' to quit and view results : "))
    while True:
        if option != "y" and option != "q":
            option = input("Invalid input !! \nEnter \'y\' for yes or \'q\' to quit and view results :")
            continue
        else:
            break
    if option == "y" :
            continue

#Histogram & progress outcome list    
    elif option == "q":
            print("-"*75)
            print("Histogram")
            print("Progress      ",progress,      ":",progress       * "*")
            print("Module Trailer",module_trailer,":",module_trailer * "*")
            print("Retreiver     ",retriever,     ":",retriever      * "*")
            print("Excluded      ",exclude,       ":",exclude        * "*")
            print(progress + module_trailer + retriever + exclude,"outcomes in total")
            print("-"*75)
            students_credits("progress      -",progress_list)
            students_credits("module_trailer-",module_trailer_list)
            students_credits("retriever     -",retriever_list)
            students_credits("exclude       -",exclude_list)
    break        

 
        
