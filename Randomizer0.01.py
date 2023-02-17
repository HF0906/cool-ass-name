#Randomizer
#Ver 0.01

import random
import time

test_text = input ("Enter the word: Roll")
test_word = str(test_text)
if str(test_text):
    print (roll())
    



def roll():
    print("Your number is:")
    for i in range(1):
        time.sleep(0.01)
        i = random.randrange(1,100)
        print(i)
        print("That is a:")
    if i>69:
         print("Success!")
    if i<70:
         print("Failure.")
    if i < 10:
         print("Very unlucky.")
    if i > 90:
         print("Very lucky!")
    

    


   

            
                
        
        

    
   

 
 
 
