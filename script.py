#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:27:57 2018

@author: Felipe Rafael de Souza
"""
import matplotlib.pyplot as plt

# @return new price based price_now
def price(price_now, amount_now):
    return (price_now - 0.1*(amount_now-500))

# @return new amount based amount_now
def amount(amount_now, price_now):
    return (amount_now + 0.2*(price_now-100))

times = 100
time = range(0,100,1)
price_init  = [100,200,100,100]
amount_init = [500,500,600,400] 

for scenario in range(len(price_init)):
    prices = []
    amounts = []
    prices.append(price_init[scenario])
    amounts.append(amount_init[scenario])
    for i in range(times):
        prices.append(price(prices[i],amounts[i]))
        amounts.append(amount(amounts[i],prices[i]))
      
    
    line_1, = plt.plot(amounts,'r',label ='amount')
    line_2, = plt.plot(prices,'b',label='price')
    plt.xlabel("time")
    plt.ylabel("prices/amount")
    plt.legend(handles=[line_1, line_2])
    plt.show()
    