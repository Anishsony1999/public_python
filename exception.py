class GopikaException(Exception):
    def __init__(self, message):
        super().__init__(message)

num = input("ENter  a Num \n")
num1 = input("Enter a num2 \n")

try:

    if num1 == '10' :
        raise GopikaException("Gopika Exception Will be there")

    ans = int(int(num)/int(num1))
    print(ans)
    print("gopika is good")
except ZeroDivisionError :
    print("Dont divis by '0' ")

except Exception as e :
    print(e)
    
finally:
    print("gopika is  too good")
    # db connection 
    # file closing 
    # importent code ending block

