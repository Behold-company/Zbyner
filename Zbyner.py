import zipfile
import locbiner
import biner

class Zbyner:
    def Lockbyner(name,new_name,password):
        locbiner.locking(password)
        eg = locbiner.q
        qp = open(f'.\\Data\\Unlocks\\{name}.zip','rb')
        a = qp.read()
        q = a.replace(b'P', f'{eg}' )
        qw = open(f'.\\Data\\Locks\\{new_name}.zip','wb')
        qw.write(q)
    def Unlockbyner(name,new_name,password):
        
        qp = open(f'.\\Data\\Locks\\{name}.zip','rb')
        a = qp.read()
        q = a.replace(password, b'P')
        qw = open(f'.\\Data\\Unlocks\\{new_name}.zip','wb')
        qw.write(q)

# https://ajabgol.ir/
# https://github.com/Behold-company
Zbyner.Lockbyner('Name', 'New name',b'Password')