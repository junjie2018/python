def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print("I have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")


describe_pet('hamster', 'harry')
describe_pet(animal_type='hamster', pet_name='harry')


def describe_pet2(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print("I have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")

describe_pet2(pet_name='whllie')
describe_pet2('while')
