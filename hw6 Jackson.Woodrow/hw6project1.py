
# Project Name:     Sphere
# Programmer:    Woodrow Jackson
#
#
# Description: a program that gives you area and volume of a sphere
#

#function to find the area of sphere
def sphereArea(radius):

    #the equation needed to find area. Used 3.14 for pi
   area= 4 *(3.14)*radius**2
   print("The area of your Sphere is : ", round(area,2))


#function to find the volume of a sphere
def sphereVolume(radius2):

    # the equation used to find the volume of a sphere 3.14 represents pi
    vol = (4/3)*(3.14)*radius2**3
    print("The Volume of a sphere is: ", round(vol, 2))

# main driver
def main():
    # the input used for the functions that are going to be called
    rad= eval(input("What is your radius for your Sphere? \nWe will give you the Volume and Area \n"
                    "Please Enter Radius: "))
    #the functions are called down here
    sphereArea(rad)
    sphereVolume(rad)

main()

