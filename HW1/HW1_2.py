# -*- coding: utf-8 -*-

stocks = int( input( "Please enter the number of stocks you wish to buy: " ) )
position = 0
stocks_to_buy = stocks / 54

for i in range( 1, 54 ):
    position += int(stocks_to_buy)
    print( "Position = %d" % position )

print( "Position = %d" % stocks )