

class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []
    def add(self, new_account):
        if not isinstance(new_account, Account):
            return False
        if any(acc.name == new_account.name for acc in self.accounts):
            return False

        self.accounts.append(new_account)
        return True


    def transfer(self, origin, dest, amount):

        if not isinstance(amount, float) and not isinstance(amount, int):
            print('Amount in bad format')
            return False

        # This prints all attributes, but I used dict instead beacuse it only has the ones defined in the class
        # print(dir(origin))

        # If requested attributes are informed and none starting with 'b' is found and each instance is well formated
        if all(key in origin.__dict__ for key in ('name', 'id', 'value')) \
                and all(any(attr.startswith(prefix) for attr in origin.__dict__) for prefix in ['addr', 'zip']) \
                and not any(attr.startswith('b') for attr in origin.__dict__) \
                and all(key in dest.__dict__ for key in ('name', 'id', 'value')) \
                and all(any(attr.startswith(prefix) for attr in dest.__dict__) for prefix in ['addr', 'zip']) \
                and not any(attr.startswith('b') for attr in dest.__dict__) \
                and isinstance(origin, Account) and isinstance(origin.name, str) and isinstance(origin.id, int) \
                and (isinstance(origin.value, float) or isinstance(origin.value, int) and len(origin.__dict__) % 2 == 1) \
                and isinstance(dest, Account) and isinstance(dest.name, str) and isinstance(dest.id, int) \
                and (isinstance(dest.value, float) or isinstance(dest.value, int) and len(dest.__dict__) % 2 == 1):
            if origin.value >= amount > 0:
                origin.transfer(-amount)
                dest.transfer(amount)
                print('{a} trasferred from {o} to {d}'.format(a=amount, o=origin.name, d=dest.name))
                return True
            print('Cannot transfer {a} from {o} to {d}. Not enough monney'.format(a=amount, o=origin.name, d=dest.name))
            return False

        print('Cannot transfer {a} from {o} to {d}. One account is corrupted'.format(a=amount, o=origin.name, d=dest.name))
        return False


    def fix_account(self, name):
        if not any([acc.name == name for acc in self.accounts]):
            print('No account with such name: [{n}'.format(n=name))
            return False

        i = [acc.name == name for acc in self.accounts].index(True)
        acc = self.accounts[i]
        print(acc.name)
        if not 'value' in acc.__dict__:
            acc.__dict__.update({'value': 0})

        if not any(attr.startswith('addr') for attr in acc.__dict__):
            print('deberia')
            acc.__dict__.update({'addr' : ''})

        if not any(attr.startswith('zip') for attr in acc.__dict__):
            acc.__dict__.update({'zip' : ''})


if __name__ == '__main__':
    john = Account('John Doe', addr='calle mis huevos', zip='ZipZap')
    jane = Account('Jane Doe', value=1000, addr=1, zip=2)
    broken = Account('Ralph')
    bank = Bank()
    bank.add(john)
    bank.add(john)
    bank.add(jane)
    bank.add(broken)
    bank.add(42)
    print(", ".join(acc.name for acc in bank.accounts))
    bank.transfer(jane, john, 100)
    print('Jane has {m1} and john has {m2}'.format(m1=jane.value, m2=john.value))

    bank.transfer(john, broken, 5)
    bank.fix_account(broken.name)
    print(dir(broken))
    bank.transfer(john, broken, 5)
