# Correct Email - xyz@gmail.com
# # Correct Password - 1234


email = input("Apna Email Bata: ")

if '@' not in email:
    email = input("Email me @ nahi hai, Apna Email phir se Bata: ")

password = input("Apna Password bhi Bata: ")

if email == "xyz@gmail.com" and password == "1234":
    print("Welcome! Login Successful ✅")

elif email == "xyz@gmail.com" and password != "1234":
    print("Login Failed, Incorrect Password ❌")
    password = input("Please Re-enter your Password: ")
    if password == "1234":
        print("Welcome! Login Successful ✅")
    else:
        print("Login Failed again, Incorrect Password ❌")

elif email != "xyz@gmail.com" and password == "1234":
    print("Login Failed, Incorrect Email ❌")
    email = input("Please Re-enter your Email: ")
    if email == "xyz@gmail.com":
        print("Welcome! Login Successful ✅")
    else:
        print("Login Failed again, Incorrect Email ❌")

else:
    print("Incorrect credentials, Login Failed ❌")

    
# # Correct Email - "xyz@gmail.com"
# # Correct Password - "1234"
