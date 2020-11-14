#File Name:     hw10project1
# Programmer:    Woodrow Jackson
# Date:          07/26/20
#
# Problem Statement:
#
#
# Overall Plan:
# 1. Create list  with account information
# 2. read accounts.txt file to create
# 3. Use list of python file words
# 4. prompt user for ID and PIN
#
#

from hw11.hw11project2.account import *

def main():

    accountList = []


    with open("accounts.txt") as file:
        for line in file:
            num = line.split(' ')

            accountList.append(Account(num[0], num[1], float(num[2]),float(num[3].replace('\n',''))))




    id = input(" Enter ID: ")
    pin = input(" Enter PIN: ")

    for acct in accountList:

        if accountList.get_id() == id:
            if accountList.get_pin() == pin:
                choice = -1

                while choice != 0:
                    print("\n Menu \n"
                          "1. Check Balance "
                          "2. Withdraw\n "
                          "3. Transfer \n"
                          "0. Exit\n")

                    choice = eval(input("Choose from Menu"))

                    if choice ==1:
                        print("\n Check Balance \n"
                              "1. Checking \n"
                              "2. Savings \n")
                        acct_type = eval(input("Choose an account (1-2): "))
                        amount = eval(input("Enter amount: "))
                        if acct.withdraw(amount, acct_type):
                            if acct_type == 1:
                                print("New Checking Balance: ", acct.get_checking())
                            else:
                                print("New Savings Balance: ", acct.get_savings())
                        else:
                            print("Insufficient funds.")
                        # choose which account to transfer to/from
                    elif choice == 3:
                        print("---Transfer---\n"
                              "1. From Checking to Savings\n"
                              "2. From Savings to Checking\n")
                        option = eval(input("Choose an option (1-2): "))
                        amount = eval(input("Enter amount:"))
                        if option == 1:
                            acct.withdraw(amount, option)
                            acct.transfer(amount, option)
                            print("New Checking Balance: ", acct.get_checking())
                            print("New Savings Balance: ", acct.get_savings())
                        else:
                            acct.withdraw(amount, option)
                            acct.transfer(amount, option)
                            print("New Savings Balance: ", acct.get_savings())
                            print("New Checking Balance: ", acct.get_checking())
                        # exit program
                    elif choice == 0:
                        break
                    else:
                        print("Invalid choice.")
                        # pin does not match

                    continue
                    # id does not match current list account
                    # check next account in list
                else:
                    continue

                    # save/write changes made to accounts.txt
                file = open("accounts.txt", 'w')
                for acct in accountList:
                    # checking and savings balance must be string
                    file.write(acct.get_id() + ' ' +
                               acct.get_pin() + ' ' +
                               str(acct.get_checking()) + ' ' +
                               str(acct.get_savings()) + "\n")
                file.close()
                print("Goodbye")

            if __name__ == '__main__':
                main()

