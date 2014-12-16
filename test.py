
class Borg:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

if __name__ == "__main__":
    a = Borg()
    a.caps = {2:'due'}
    b = Borg()
    b.caps.update({3:'tre'})
    print b.caps