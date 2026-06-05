N =input("Enter Student Name:")
T =int(input("Enter Your Tamil Mark:"))
E =int(input("Enter Your English Mark:"))
M =int(input("Enter Your Maths Mark:"))
S =int(input("Enter Your Science Mark:"))
L =int(input ("Entre Your Social Science Mark:"))
Total = T+E+M+S+L 
avg =(Total/5)
print ("-------STUDENT REPORT --------")
print("Your Name Is:",N)
print("Your Five Subject Total Is:",Total)
print("Your Average Is:",round(avg,2))
print("Your Percentage:",round((Total/500)*100,2),"%")
if(T<35 or E<35 or M<35 or S<35 or L<35):
    print ("Result:Fail")
    print("Your Grade is:F")
else:
    if(avg>=35 and avg<=50):
        print("Your Grade is:D")
    elif(avg<=70):
        print("Your Grade is:C")
    elif(avg<=80):
        print("Your Grade is:B")
    elif(avg<=90):
        print("Your Grade is:A")
    else:
        print("Your Grade is:A+")  

    print("Result:PASS")  
    
    




    
     
        
