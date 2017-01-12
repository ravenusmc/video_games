#This class will have all of the support functions that I use in the program.
#I may be over doing using classes and objects but it is helping me understand
#how to use objects and classes.

class Support():

    #This method will be displayed if the user quits from the program. 
    def quit(self):
        print("\033c")
        print('Sorry you don"t want to use the program')
        print('Maybe next time...Good Bye!')
        print()
