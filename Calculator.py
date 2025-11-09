def sum(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

def avg(n1,n2):
    return n1+n2/2

print("select any no.which is valid")
print("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Average")
select=int(input("enter no. which is available our list: "))
if(select in [1,2,3,4,5]):
    number1=float(input("enter first no."))
    number2=float(input("enter second no."))
    if(select==1):
        
        print("Addition of no.",number1,"+",number2,sum(number1,number2))
    elif(select==2):
         print("Subtraction of no.",number1,"-",number2,sub(number1,number2))
    elif(select==3):
         print("Multiplication of no.",number1,"*",number2,mul(number1,number2))
    elif(select==4):
         print("Division of no.",number1,"/",number2,div(number1,number2))
    elif(select==5):
         print("Average of no.",number1,"%",number2,avg(number1,number2))
else:
    print("no. is not valide")

