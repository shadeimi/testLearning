
import ZODB.DB
from account import Account
import BTrees.OOBTree
import transaction


class testGenerator():
    
    def __init__(self):
        self.storage = ZODB.DB(None)
        self.connection = self.storage.open()
        self.root = self.connection.root
        self.root.accounts = BTrees.OOBTree.BTree()
        

    def manager(self, accountName, account):
        try:
            self.root.accounts[accountName] = account
            transaction.commit()
        except Exception as e:
            print str(e.message)
            transaction.abort()
            pass
        
    def extract(self, accountName):
        try:
            return self.root.accounts[accountName]
        except (AttributeError, KeyError) as e:
            print "Key Error, %s doesn't exist." % accountName
            exit(-1)
            

if __name__ == "__main__":
    tg = testGenerator()
    a = Account()
    a.deposit(100)
    tg.manager('nello', a)
    
    print tg.extract('nello').balance
