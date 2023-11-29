def myfunc():
    print("This is python function which is not similar with shell script,")
    print("For trying purpose only")

myfunc()

def reverse_string(str):  
    str1 = ""   # Declaring empty string to store the reversed string  
    for i in str:  
        str1 = i + str1  
    return str1    # It will return the reverse string to the caller function  
     
str = "JavaTpoint"    # Given String       
print("The original string is: ",str)  
print("The reverse string is",reverse_string(str)) # Function call  


str = "JavaTpoint" #  string variable  
print ("The original string  is : ",str)   
reverse_String = ""  # Empty String  
count = len(str) # Find length of a string and save in count variable  
while count > 0:   
    reverse_String += str[ count - 1 ] # save the value of str[count-1] in reverseString  
    count = count - 1 # decrement index  
print ("The reversed string using a while loop is : ",reverse_String)# reversed string  


def usernp():
    print("my user is Hosaraf")
    print("my password is msdfd934")

usernp()

print("User name is usermind")
print("password is mypasswd")





