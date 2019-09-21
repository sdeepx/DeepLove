from Algo import lovealgo
from banner import lovesym

__author__ = "Shubhadeep"
__version__ = 0.2


lovesym.symbol()


def main():
    lovesym.row()
    yname = lovesym.yname()
    print()
    lname = lovesym.lname()
    percentage = lovealgo.love_algo(yname, lname)
    percentage1 = lovealgo.love_algo(lname, yname)

    print(" ")
    print("You love", lname, percentage, "%")
    print(lname, "loves you", percentage1, "%")

    if percentage > percentage1:
        print(" ")
        print(lname, " should love you more ")
        lovesym.row()
    elif percentage1 > percentage:
        print(" ")
        print(yname, "-- You should love ", lname, " more ")
        lovesym.row()
    elif percentage == percentage1:
        print(" ")
        print("WOW! you are awesome ! :)  ")
        lovesym.row()
    else:
        print("sorry! Something went wrong!")
        lovesym.row()

    def again():
        do_again = input("Do you want to check your love percentage again? 'y' or 'n' ")
        print(" ")
        len_do_again = len(do_again)
        if len_do_again == 0:
            print("[-] Ops! I think you forgot to enter an option ")
            return again()
        if do_again == "y":
            return main()
        elif do_again == "n":
            print("OK! thank you ")

        else:
            print("[-] Umm! you chose a wrong option. \n [*] Please choose a right option \n")
            return again()

    if __name__ == '__main__':
        again()


if __name__ == "__main__":
    main()
