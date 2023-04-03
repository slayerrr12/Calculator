import operations


def calculator(a):
    if(a==1):
        operations.add()
    if(a==2):
        operations.subtract()
    if(a==3):
        operations.multiply()
    if(a==4):
        operations.divide()



def main():
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.EXIT")
    
    a = int(input("write the number of operation you want to do:"))
    calculator(a)
        
    return a
   
while(True):
    a = main()
    if a==5:
        print("EXITING.....")
        break







