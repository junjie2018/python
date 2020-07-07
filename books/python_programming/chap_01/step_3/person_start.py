class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return '<%s => %s>' % (self.__class__.__name__, self.name)


class Manager(Person):
    # def give_raise(self, percent, bonus=0.1):
    #     self.pay *= (1.0 + percent + bonus)
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def give_raise(self, percent, bonus=0.1):
        Person.give_raise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')

    print("###### TEST ######")
    print(bob.name, sue.pay)
    print(bob.last_name())
    sue.give_raise(.10)
    print(sue.pay)

    print("\n###### TEST ######")
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom.last_name())
    tom.give_raise(.20)
    print(tom.pay)

    print("\n###### TEST ######")
    db = [bob, sue, tom]
    for obj in db:
        obj.give_raise(.10)
    for obj in db:
        print(obj.last_name(), '=>', obj.pay)

    print("\n###### TEST ######")
    print(tom)
