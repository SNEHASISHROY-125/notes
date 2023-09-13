# class Animal:
#     def __init__(self):
#         self.eyes = 2
#     def brethe(self):
#         print('Inhele ,Exhale.')


# class Duck(Animal):            # Inheriting everything inside class Animal.
#     def eats(self):
#         print('Eats insect.')
    
#     def sleep(self):
#         print('Sleeps not under water.')
    
#     def sound(self):
#         print('Pack! Pack!')


# class Dog(Animal):  
#     def breth(self):
#         super().brethe()            #### Super() class is the inherite class , here it is Animal.
#         print('On the ground.')     ## Here used to modify the func.v'

#     def eats(self):
#         print('Can eat human poop.')
    
#     def sleep(self):
#         print('Sleeps not under water.')

#     def sound(self):
#         print('Barks.')
    
    
 
# poly = Duck()
# poly.brethe()
# print('Has eyes:' , poly.eyes)
# poly.eats()
# poly.sleep()
# poly.sound()

# dogo = Dog()
# dogo.breth()
# print('Has eyes:' , dogo.eyes)
# dogo.eats()
# dogo.sound()



class father_class:
    nt = 'initialize'

    def father(self):
        print('from father')


class Child_class(father_class):
    def __init__(self):
        super().__init__()

    def child(self):
        print('from child class' + super().nt)
        # super().father()


call = Child_class()
call.child()
