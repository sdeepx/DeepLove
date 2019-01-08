import random
def love(you, lover):
    len1 = len(you)
    len2 = len(lover)
    per = random.randint(80,90)
    per2 = random.randint(80,100)
    per3 = random.randint(30,60)
    per4 = random.randint(2,4)
    parcentage = ((len1 + per2 /per4) / (len2 + per3))*per
    return parcentage

def main():
    yname = input("Enter your name: ")
    lname = input("Enter your lover's or ladylove's name : ")
    parcentage = love(yname, lname)
    parcentage1 = love(lname, yname)

    print(" ")
    print("You love",lname,parcentage,"%")
    print(lname,"loves you",parcentage1,"%")

    if parcentage > parcentage1:
        print(" ")
        print(lname, " should love you more ")
        print(" ")
    elif parcentage1 > parcentage:
        print(" ")
        print(yname, "-- You should love ", lname, " more ")
        print(" ")
    elif parcentage == parcentage1:
        print(" ")
        print("WOW! you are awesome ! :)  ")
        print(" ")
    else:
        print("sorry! Something went wrong!")
        print(" ")

    def again():
        again = input("Do you wnat to check your love percentage again? 'y' or 'n' ")
        print(" ")
        if again == "y":
            return main()
        elif again == "n":
            print("OK! thank you ")

        else:
            print("Sorry something went wrong! you did enter the right value..")

    again()

if __name__ == "__main__":
    main()