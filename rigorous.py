import random
import string
import argparse
import sys
import os



def rigorous():
    password = sys.argv[1]
    length = (len(password))
    chars   = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    print (length, "Words")
    
    if length ==0:
        print ("Input Your Password!")
    elif length < 6:
        print ("Min 6 Words")
        print ("Failure!")
    elif length ==6:
        print (''.join(random.choice(chars) for i in range(12)))
        print ("Ecnrypted! \n")
    elif length < 12:
        print (''.join(random.choice(chars) for i in range(24)))
        print ("Ecnrypted! \n")
    elif length < 16:
        print (''.join(random.choice(chars) for i in range(32)))
        print ("Ecnrypted! \n")
    elif length < 32:
        print (''.join(random.choice(chars) for i in range(64)))
        print ("Ecnrypted! \n")
    else:
        print (''.join(random.choice(chars) for i in range(128)))
        print ("Ecnrypted! \n")


if __name__ == "__main__":


    os.system("clear")
    print ("""
   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ 
 ( R | i | g | o | r | o | u | s )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/  v1.0
  
  Contact:
      https://github.com/tellcyber
      https://t.me/tellcy13er
      https://instagram.com/tellcyber
""")
    rigorous()
