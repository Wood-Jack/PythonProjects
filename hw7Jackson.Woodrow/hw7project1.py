

# Project Name:    aChildsHeight
# Programmer:    Woodrow Jackson
#
#
# Description: a program that gives you the height of the child from the parents
#

def main():
    print("Welcome to the height shop we can tell you the height of your child \n"
          "if your trying to say 5'7 or 6'1 (EX) 5.7 , 6.1 \n")

    #orginal takes in the feet of the two adults
    hDad= eval(input("Would the dad please enter your height"))

    #converting the feet into inches of adults
    adultHConvert1 = hDad*12

    hMom= eval(input("Would the mom please enter your height "))
    adultHConvert2 = hMom*12

    #using a number to determine if its a boy or girl
    gender = eval(input("Is the baby boy or girl. Press 1) Boy  Press 2) Girl"))

    if gender  == 1:
        hBoy = (((hMom * 13/12) + hDad)/2)

        #connverting to inches
        convertedToInches= hBoy *12

        print("Dad Height Feet: ", hDad, " Inches: ", adultHConvert1, "\n"
             "Mom Height Feet: ", hMom, " Inches: ",  adultHConvert2, "\n"
            "Son Height Feet: ", round(hBoy,1), "Inches:", round(convertedToInches,1))

    if gender == 2:
        hGirl = ((hDad * 12 / 13) + hMom) / 2

        #convert To inches
        convertedToInches = hGirl * 12



        print("Dad Height Feet: ",hDad," Inches: ", adultHConvert1,"\n"
              "Mom Height Feet: ",hMom," Inches: ", adultHConvert2,"\n"
              "Daughter Height Feet: ", round(hGirl,1) ,"Inches:", round(convertedToInches,1))

main()