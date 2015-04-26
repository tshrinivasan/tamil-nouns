#-*- coding: utf-8 -*-



import sys
import tamil
import os

namelist = open(sys.argv[1], 'rt')

for name in namelist:
    name_uni = unicode(name,"utf-8")
    letters = tamil.utf8.get_letters(name_uni)
    first_letter =  letters[0]
    
    if not os.path.exists(first_letter):
        open(first_letter,'w').close()


    if os.path.isfile(first_letter):    
        namefile = open(first_letter, "a")
        namefile.write(name_uni.encode('utf-8'))

