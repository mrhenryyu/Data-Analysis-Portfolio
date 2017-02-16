# random password generator

import sys
import re
import random

def main():
    args = sys.argv[1:]

    weak_list = ["apple", "banana" ,"carrot", "date", "eggs", "fruits"]
    user= input("How strong do you want your password? Weak, or strong?")
    
    if user == "weak":
        p_choice = random.randint(0, len(weak_list)-1)
        print("Your password is:")
        print (weak_list[p_choice])

    else:
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        passlen = 8
        p = "".join(random.sample(s,passlen))
if __name__ == '__main__':
  main()

