# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sold):
    pet_shop["admin"]["pets_sold"] += sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop,breed):
    breed_count = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breed_count.append(pet)
    return breed_count

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
    return None

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)
            return

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append("new_pet")

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
