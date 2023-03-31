import random        
import time

print("Version 0.2")
print("Do you want to Login  1 YES/2 NO?")  
number = input(">>")         
print("")
text1 = input("Type your Username >")   
t = text1.lower()
print("")         

if text1 == "test1":     
        text2 = input("Type your Password >")       
        t = text2.lower()

if text2 == "test2":    
        print("")
        print("hello test")  
       
else:
    print("Your Username or Password is Wrong!")    
    print("Try Again")                              

time.sleep(10);      



