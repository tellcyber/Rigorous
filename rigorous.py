import random
import string
import argparse
import sys
import os
import argparse



def rigorous():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--list-type", action="store_true", help="Print List of Type Password")
        parser.add_argument("-t", "--type", help="Type Of Password, see --list-type for more", type=int)
        parser.add_argument("-w", "--words", help="Write Your Password")
        parser.parse_args()
        args = parser.parse_args()
        pwd = args.words
        if args.list_type:
            print("""
        List Type for Encrypt
            1 = For Lowercase and Uppercase
            2 = For Lowercase and Digits
            3 = For Uppercase and Digits
            4 = For Lowercase, Uppercase and Digits
            5 = For Lowercase, Uppercase, Digits and Punctuation
            
            lowercase   = abcdefghijklmnopqrstuvwxyz
            uppercase   = ABCDEFGHIJKLMNOPQRSTUVWXYZ
            digits      = 0123456789
            punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")
        chars1 = string.ascii_lowercase + string.ascii_uppercase
        chars2 = string.ascii_lowercase + string.digits
        chars3 = string.ascii_uppercase + string.digits
        chars4 = string.ascii_lowercase + string.ascii_uppercase + string.digits
        chars5 = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        length = (len(pwd))
        print (length, "Words")


        if length ==0:
            print ("Input Your Password!")
        elif length < 6:
            print ("Min 6 Words")
        elif args.type ==1 and length ==6:
            print (''.join(random.choice(chars1) for i in range(12)))
            print ("Ecnrypted! \n")
        elif args.type ==1 and length < 13:
            print (''.join(random.choice(chars1) for i in range(24)))
            print ("Ecnrypted! \n")
        elif args.type ==1 and length < 17:
            print (''.join(random.choice(chars1) for i in range(32)))
        elif args.type ==1 and length < 33:
            print (''.join(random.choice(chars1) for i in range(64)))
            print ("Ecnrypted! \n")
        elif args.type ==2 and length ==6:
            print (''.join(random.choice(chars2) for i in range(12)))
            print ("Ecnrypted! \n")
        elif args.type ==2 and length < 13:
            print (''.join(random.choice(chars2) for i in range(24)))
            print ("Ecnrypted! \n")
        elif args.type ==2 and length < 17:
            print (''.join(random.choice(chars2) for i in range(32)))
            print ("Ecnrypted! \n")
        elif args.type ==2 and length < 33:
            print (''.join(random.choice(chars2) for i in range(64)))
            print ("Ecnrypted! \n")
        elif args.type ==3 and length ==6:
            print (''.join(random.choice(chars3) for i in range(12)))
            print ("Ecnrypted! \n")
        elif args.type ==3 and length < 13:
            print (''.join(random.choice(chars3) for i in range(24)))
            print ("Ecnrypted! \n")
        elif args.type ==3 and length < 17:
            print (''.join(random.choice(chars3) for i in range(32)))
            print ("Ecnrypted! \n")
        elif args.type ==3 and length < 33:
            print (''.join(random.choice(chars3) for i in range(64)))
            print ("Ecnrypted! \n")
        elif args.type ==4 and length ==6:
            print (''.join(random.choice(chars4) for i in range(12)))
            print ("Ecnrypted! \n")
        elif args.type ==4 and length < 13:
            print (''.join(random.choice(chars4) for i in range(24)))
            print ("Ecnrypted! \n")
        elif args.type ==4 and length < 17:
            print (''.join(random.choice(chars4) for i in range(32)))
            print ("Ecnrypted! \n")
        elif args.type ==4 and length < 33:
            print (''.join(random.choice(chars4) for i in range(64)))
            print ("Ecnrypted! \n")
        elif args.type ==5 and length ==6:
            print (''.join(random.choice(chars5) for i in range(12)))
            print ("Ecnrypted! \n")
        elif args.type ==5 and length < 13:
            print (''.join(random.choice(chars5) for i in range(24)))
            print ("Ecnrypted! \n")
        elif args.type ==5 and length < 17:
            print (''.join(random.choice(chars5) for i in range(32)))
            print ("Ecnrypted! \n")
        elif args.type ==5 and length < 33:
            print (''.join(random.choice(chars5) for i in range(64)))
            print ("Ecnrypted! \n")
        elif length > 32:
            print ("Max 32 Words!")   
    except UnboundLocalError:
        pass
    except TypeError:
        pass

if __name__ == "__main__":


    print ("""
   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ 
 ( R | i | g | o | r | o | u | s )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/  v2.4
  
  Contact:
      https://github.com/tellcyber
      https://t.me/tellcy13er
      https://instagram.com/tellcyber
""")
    rigorous()

