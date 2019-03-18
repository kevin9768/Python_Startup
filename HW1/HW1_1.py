# -*- coding: utf-8 -*-

revenue = float(input( "Please enter TSMC's fourth quarter revenue( 100 million ): " ))

if revenue > 84.9 * 1.1 :
    print("買進")
elif revenue >= 84.9 :
    print("不買賣")
else:
    print("賣出")