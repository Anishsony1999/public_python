
def f1():
    # this function return a Function
    coins =10

    def play():
        nonlocal coins
        coins -= 1
        print(coins)
    
    return play

gopika = f1() #10
bhoomika = f1() #10

gopika()
gopika()
gopika()
gopika()
gopika()
bhoomika()
bhoomika()
