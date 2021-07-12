"""Turn English into Pig Latin"""
import sys

vowels = 'aeiou'

#while loop
while True:
    word = input("type a word and get its Pig Latin translation: ")

    #if word starts with vowal add way to end 
    if word[0] in vowels:
        pig_Latin = word + 'way'
    #else add ay
    else:
        pig_Latin = word[1:] + word[0] + 'ay'
    print()
    print("{}".format(pig_Latin), file=sys.stderr)

   #ask user if they want to play again
    try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
    if try_again.lower() == "n":
        break #ends loop

input("\nPress Enter to exit.\n")


