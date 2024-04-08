# DaniePratt 4-9-24
# this program creates a "Flower" class defining the initializing method __init_ and defining another 2 methods "grow" and "bloom" it then defines tha main function where 2 flower objects are creaed and each method is called.

#flower class creation
class Flower:
    # initialization
    def __init__(self, name):
        self.name = name
	# method 1 uses the print function to concatanate the object in the middle of a phrase
    def grow(self):
        print("The " +self.name + " is growing.")
	# method 2 uses the print function to do the same but this time the flower blooms
    def bloom(self):
        print("The " + self.name + " is blooming.")
# define main function
def main():
	# creation of flower object "Rose"
    flower1 = Flower("Rose")
    # flower 1 calls method "grow"
    flower1.grow()
    # flower 1 callse method "bloom"
    flower1.bloom()
    # creation of flower object "Daisy"
    flower2 = Flower("Daisy")
    # flower 2 calls method "grow"
    flower2.grow()
    # # flower 2 callse method "bloom"
    flower2.bloom()
# condition to check all functions of program completed
if __name__ == "__main__":
  main()
