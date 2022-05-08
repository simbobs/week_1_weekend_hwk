# WRITE YOUR FUNCTIONS HERE
import pdb

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, number):
    pet_shop["admin"]["total_cash"] += number
 
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] += pets_sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    breeds_found=[]
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breeds_found.append(pet)
    return breeds_found
    print(len(breeds_found))

def find_pet_by_name(pet_shop, name):
    pet_name = None
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_name = pet
    return pet_name

def remove_pet_by_name(pet_shop, name):
    list_of_pets = pet_shop["pets"]
    for pet in list_of_pets:
        if pet["name"] == name:
            list_of_pets.remove(pet)

            
def add_pet_to_stock(pet_shop, new_pet):
    list_of_pets = pet_shop["pets"]
    list_of_pets.append(new_pet)
    return list_of_pets
    len(list_of_pets)
    
def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, money):
    customer["cash"] -= money

def get_customer_pet_count(customer):
    number_of_pets = customer["pets"]
    return len(number_of_pets)
    

def add_pet_to_customer(customer, new_pet):
    list_of_pets = customer["pets"]
    list_of_pets.append(new_pet)

def customer_can_afford_pet(customer,new_pet):
    can_afford_pet = False
    if customer["cash"] >= new_pet["price"]:
        can_afford_pet = True
    return can_afford_pet


        
        
        
    
    
    
    
    
        
        
   
    
       
       
    
        
        
        
        
        
    


    
    
            
            
            
            
        
    
            
            


    
   
    
   

    

    




    
    

   
    