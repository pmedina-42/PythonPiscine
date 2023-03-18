

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


        if isinstance(origin, str) and isinstance(dest, str):
            for acc in self.accounts:
                if acc.name == origin:
                    o = acc
                if acc.name == dest:
                    d = acc
        else:
           return False

        if isinstance(o, Account) and isinstance(d, Account):
            # If both origin and dest accounts have the necessary fields
            if all(key in o.__dict__ for key in ('name', 'id', 'value')) \
                    and all(any(attr.startswith(prefix) for attr in o.__dict__) for prefix in ['addr', 'zip']) \
                     and not any(attr.startswith('b') for attr in o.__dict__) \
                    and all(key in d.__dict__ for key in ('name', 'id', 'value')) \
                    and all(any(attr.startswith(prefix) for attr in d.__dict__) for prefix in ['addr', 'zip']) \
                    and not any(attr.startswith('b') for attr in d.__dict__) \
                    and isinstance(o.name, str) and isinstance(o.id, int) \
                    and (isinstance(o.value, float) or isinstance(o.value, int) and len(o.__dict__) % 2 == 1) \
                    and isinstance(d.name, str) and isinstance(d.id, int) \
                    and (isinstance(d.value, float) or isinstance(d.value, int) and len(d.__dict__) % 2 == 1):
                if o.value >= amount > 0:
                    o.transfer(-amount)
                    d.transfer(amount)
                    print('{a} trasferred from {o} to {d}'.format(a=amount, o=origin, d=dest))
                    return True
                print('Cannot transfer {a} from {o} to {d}. Not enough monney'.format(a=amount, o=origin, d=dest))
                return False

            else:
                return False

        # This prints all attributes, but I used dict instead beacuse it only has the ones defined in the class
        # print(dir(origin))

        # If requested attributes are informed and none starting with 'b' is found and each instance is well formated

        print('Cannot transfer {a} from {o} to {d}. One account is corrupted'.format(a=amount, o=origin.name, d=dest.name))
        return False


    def fix_account(self, name):
        if not any([acc.name == name for acc in self.accounts]):
            print('No account with such name: [{n}'.format(n=name))
            return False

        i = [acc.name == name for acc in self.accounts].index(True)
        acc = self.accounts[i]
        if not 'value' in acc.__dict__:
            acc.__dict__.update({'value': 0})

        if not any(attr.startswith('addr') for attr in acc.__dict__):
            acc.__dict__.update({'addr' : 'addr'})

        if not any(attr.startswith('zip') for attr in acc.__dict__):
            acc.__dict__.update({'zip' : 'zip'})

        if len(acc.__dict__) % 2 != 1:
            acc.__dict__.update({'filler': ''})
        return True


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
