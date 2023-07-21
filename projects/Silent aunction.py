
print("<<----------------( WELCOME TO AUNCTIONS! )-------------------->>")
import os
def main():
    auction=dict()
    while True:
        name=(input("What is your name? "))
        bit=int(input("What is your bit? "))
        auction[name]=bit
        choice=str(input("Do you want to continue?(yes/no)? ")).lower()
        if choice=="yes":
            os.system("cls")
            pass
        if choice=="no":
            maxi=0
            for i,j in auction.items():
                if j >maxi:
                    maxi=j
                    max_ele=i
            print()
            print("-------CONGRATULATIONS!--------")
            print(f'The highest bit is of {maxi} by {max_ele}')  
            print()
            break
main()


#new_learning
#import os -----> os.system("cls") for clearing screen
