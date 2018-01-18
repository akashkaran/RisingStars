class Person:
    def __init__(self,id):
        self.id=id
        obama=Person(100)
        obama.__dict__['age']=49
        a=len(obama.__dict__)
        print(a)
