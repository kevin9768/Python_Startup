# -*- coding: utf-8 -*-


num = int(input( "Enter a 5-digit number: " ))

if int(num / 10000) == num % 10 and (int(num / 1000)) % 10 == int((num % 100) / 10) :
    print( "True" )
else:
    print( "False" )