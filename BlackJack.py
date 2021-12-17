#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 21:15:01 2020

@author: efgar1
"""

import random
import itertools
import numpy as np

#create deck
deck = ["2 of Hearts", "2 of Spades",     "2 of Diamonds", "2 of Clubs",
        "3 of Hearts", "3 of Spades",     "3 of Diamonds", "3 of Clubs",
        "4 of Hearts", "4 of Spades",     "4 of Diamonds", "4 of Clubs",
        "5 of Hearts", "5 of Spades",     "5 of Diamonds", "5 of Clubs",
        "6 of Hearts", "6 of Spades",     "6 of Diamonds", "6 of Clubs",
        "7 of Hearts", "7 of Spades",     "7 of Diamonds", "7 of Clubs",
        "8 of Hearts", "8 of Spades",     "8 of Diamonds", "8 of Clubs",
        "9 of Hearts", "9 of Spades",     "9 of Diamonds", "9 of Clubs",
        "10 of Hearts", "10 of Spades", "10 of Diamonds", "10 of Clubs",
        "J of Hearts", "J of Spades",     "J of Diamonds", "J of Clubs",
        "Q of Hearts", "Q of Spades",     "Q of Diamonds", "Q of Clubs",
        "K of Hearts", "K of Spades",     "K of Diamonds", "K of Clubs",
        "A of Hearts", "A of Spades",     "A of Diamonds", "A of Clubs"]

#random.shuffle(deck)

#total combiniations are 78

Dhand = []
Phand = []
Pstart = []
Pstart1 = []
Pstart2 =[]
valList = []
DwinList = []
PwinList = []
TieList = []
        
uniqValList = [2,3,4,5,6,7,8,9,10,10,10,10,11]

uniqValListD = [2,3,4,5,6,7,8,9,10,10,10,10,11]

Pstart1 = list(itertools.combinations(uniqValList, 2))

def Dstart(x,s):
    Dhand = [[x,s]]
    if x ==11 and s == 11 in Dhand[0]:
        s = 1
    return Dhand

def dealer():
    return valList[0]

def player():
    return valList[0]
                
for q in range(len(Pstart1)):
    #print("Pstat1 at q = ",q,"is",Pstart1[q])
    Pstart.append(list(Pstart1[q]))

for s in uniqValListD:
    #Makeing sure to go through all the starting hands
    for n in range(1):
    
    #######################################
    # Create new deck for a new game
        for i in range(52):
            if "2" in deck[i]:
                valu = 2
                valList.append(valu)
            if "3" in deck[i]:
                valu = 3
                valList.append(valu)
            if "4" in deck[i]:
                valu = 4
                valList.append(valu)
            if "5" in deck[i]:
                valu = 5
                valList.append(valu)
            if "6" in deck[i]:
                valu = 6
                valList.append(valu)
            if "7" in deck[i]:
                valu = 7
                valList.append(valu)
            if "8" in deck[i]:
                valu = 8
                valList.append(valu)
            if "9" in deck[i]:
                valu = 9
                valList.append(valu)
            if "10" in deck[i]:
                valu = 10
                valList.append(valu)
            if "J" in deck[i]:
                valu = 10
                valList.append(valu)
            if "Q" in deck[i]:
                valu = 10
                valList.append(valu)
            if "K" in deck[i]:
                valu = 10
                valList.append(valu)
            if "A" in deck[i]:
                valu = 11
                valList.append(valu)
            
        random.shuffle(valList)
    #########################################
        Phand.append(Pstart[n])
        Pstart2 = Pstart[n]
        a = Pstart[0][0]
        b = Pstart[0][1]
        valList.remove(a)
        valList.remove(b)
    
    # Number of Rounds ############################
    
        for m in range(10):
            print("-------------------------------------------------------------------")
            print("Dealer is showing",s, "Game",n)
            print(" ")
            print(valList)
            print(" ")
            print("Player's starting hand", Phand)
            y = random.randint(2,11)
            Dhand = Dstart(y,s)
            c = Dhand[0][0]
            d = Dhand[0][1]
            valList.remove(c)
            valList.remove(d)
            print("Dealer's starting hand", Dhand)
        
    # Player ######################################
        
            while sum(Phand[0]) < 21:
                Phand[0].append(player())
                valList.remove(valList[0])
                print(" ")
                print("Player's hand is", Phand[0],". Total is", sum(Phand[0]))
                print(" ")
                if 14 < sum(Phand[0]) < 21:
                    if 11 in Phand[0]:
                        print(" ")
                        print("There is an eleven in the player's hand!", Phand[0].index(11))
                        print(" ")
                        x = Phand[0].index(11)
                        Phand[0][x] = 1
                        break
                    else:
                        break
                    
                #if player busts, Dealer wins 
                
                if sum(Phand[0])>21:
                    print(" ")
                    print("Dealer wins!") 
                    print(" ")
                    print("Dealer showed a(n)", s," while the player started with",[Phand[0][0],Phand[0][1]])
                    print(" ")
                    DwinList.append([[Phand[0][0],Phand[0][1]],s])
                    break
                    
    # Dealer ######################################
    
            if sum(Phand[0])>21:
                break
            while sum(Dhand[0]) < 21:
                Dhand[0].append(dealer())  
                valList.remove(valList[0])
                print(" ")
                print("Dealer's hand is", Dhand[0],". Total is", sum(Dhand[0]))
                print(" ")
                
                #if Dealer is over 21 and has an eleven
                
                if sum(Dhand[0]) > 21:
                    if 11 in Dhand[0]:
                        print(" ")
                        print("There is an eleven in the dealer's hand!", Dhand[0].index(11))
                        print(" ")
                        x = Dhand[0].index(11)
                        Dhand[0][x] = 1
                        break
                    
                    #if dealer busts, Player wins
                    
                    print(" ")
                    print("Player wins!") 
                    print(" ")
                    print("Dealer showed a(n)", s," while the player started with",[Phand[0][0],Phand[0][1]])
                    
                    PwinList.append([[Phand[0][0],Phand[0][1]],s])
                    break
                if 17 <= sum(Dhand[0]) <= 21:
                    break
        
    # end #########################################
        
            if 17 <= sum(Dhand[0]) <= 21 and 15 <= sum(Phand[0]) <= 21:
               
                if sum(Dhand[0]) ==sum(Phand[0]):
                    print(" ")
                    print("It's a tie! Nobody wins") 
                    print(" ")
                    print("Dealer showed a(n)", s," while the player started with",[Phand[0][0],Phand[0][1]])
                    print(" ")
                    TieList.append([[Phand[0][0],Phand[0][1]],s])
                
                #if player has lower hand value, Dealer wins
                
                if sum(Phand[0])<sum(Dhand[0])<=21:
                    print(" ")
                    print("Dealer wins!") 
                    print(" ")
                    print("Dealer showed a(n)", s," while the player started with",[Phand[0][0],Phand[0][1]])
                    print(" ")
                    DwinList.append([[Phand[0][0],Phand[0][1]],s])
                
                #if player has higher hand value, Player wins   
                 
                if sum(Dhand[0])<sum(Phand[0]):
                    print(" ")
                    print("Player wins!") 
                    print(" ")
                    print("Dealer showed a(n)", s," while the player started with",[Phand[0][0],Phand[0][1]])
                    print(" ")
                    PwinList.append([[Phand[0][0],Phand[0][1]],s])
                break
    
        # print("Player's hand is", Phand[0],". Total is", sum(Phand[0]))
        # print(" ")
        #print("Dealer's hand is", Dhand[0], ". Total is",sum(Dhand[0]))
        # print("the value,",a ,", appears", valList.count(a), "times")
        # print("the value,",b ,", appears", valList.count(b), "times")
        print(" ")
        
        Phand = []
        Dhand[0] = []
        valList = []

print("total games: ", len(DwinList)+len(PwinList)+len(TieList))
print("There should be 78*11 = 858 games")
        
print ("========================================================")
print("Total Player wins with Data:",PwinList)
print(" ")
print("Total Dealer wins with Data:",DwinList)
print ("========================================================")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    









