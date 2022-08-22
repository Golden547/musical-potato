# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 19:24:30 2022

@author: shn99
"""

class parent():
    def __init__(self):
        print("This is a parent class")
        
    def menu(dish):
           if dish=="burger":
               print("You can add the following toppings")
               print("More cheese | Add jalapeno")
           elif dish =="iced americano":
               print("You can add the following toppings")
               print("Add Chocolate | Add caramel")
           else:
               print("Please enter valid dish")
    
    def final_amount(dish,add_ons):
        if dish=="burger" and add_ons=="cheese":
            print("you need to pay 250 USD")
        elif dish=="burger" and add_ons=="jalapeno":
            print("You need to pay 350 USD")
        elif dish=="iced_americano" and add_ons=="chocolate":
            print("you need to pay 250 USD")
            print("You need to pay 350 USD")
        elif dish=="iced-american" and add_ons=="caramel":
            print("you need to pay 450 USD")
        
class child1(parent):
    def __init__(self,dish,addons):
        self.newdish=dish
        self.addons = addons
    def get_menu(self):
        parent.menu(self.new_dish)
        
class child2(parent):
    def __init(self,dish,addons):
        self.new_dish=dish
        self.addons = addons
    
    def get_final_amount(self):
        parent.final_amount(self.new_dish,self.addons)
        

    
child1_object=child1("burger")
child1_object.get_menu()

child2_object=child2("burger","jalapeno")
child2_object.get_final_amount()



        
             
        