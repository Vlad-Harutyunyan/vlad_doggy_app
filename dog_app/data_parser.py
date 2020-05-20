import requests
import json

def load_data(url) :
    # thisfolder = os.path.dirname(os.path.abspath(__file__))
    # initfile = os.path.join(thisfolder, filename)
    return requests.get(url).json()

class Dog:
    def __init__(self):
        self.name = None
        self.weight = None
        self.height = None
        self.id = None
        self.bread_for = None
        self.breed_group = None
        self.life_span = None
        self.temperament = None
        self.origin = None
    #setters
    def set_name(self,inp):
        self.name = inp
    def set_weight(self,inp):
        self.weight = inp
    def set_height(self,inp) :
        self.height = inp
    def set_id(self,inp):
        self.id = inp
    def set_bread_for(self,inp) :
        self.bread_for = inp
    def set_breed_group(self,inp) :
        self.breed_group = inp
    def set_life_span(self,inp) :
        self.life_span = inp
    def set_temperament(self,inp):
        self.temperament = inp
    def set_origin(self,inp):
        self.origin = inp
    def test(self):
        print(  f' Hi i`m {self.name} , i`m from {self.origin}'  )


def Parse_to_list():
    info = load_data('https://api.thedogapi.com/v1/breeds')

    dog_list = []

    #set data
    for x in range(1,len(info)):
        doggy = Dog()
        #set name
        try :
            inp = info[x]['name']
            doggy.set_name(inp)
        except:
            pass
        #set weight
        try :
            inp = info[x]['weight']['metric']
            doggy.set_weight(inp)
        except:
            pass
        #set height
        try :
            inp = info[x]['height']['metric']
            doggy.set_height(inp)
        except:
            pass
        #set id
        try :
            inp = info[x]['id']
            doggy.set_id(inp)
        except:
            pass
        #set bred for 
        try :
            inp = info[x]['bred_for']
            doggy.set_bread_for(inp)
        except:
            pass
        #set breed group
        try :
            inp = info[x]['breed_group']
            doggy.set_breed_group(inp)
        except:
            pass
        #set life span
        try :
            inp = info[x]['life_span']
            doggy.set_life_span(inp)
        except:
            pass
        #set temperament
        try :
            inp = info[x]['temperament']
            doggy.set_temperament(inp)
        except:
            pass
        # set origin
        try :
            inp = info[x]['origin']
            doggy.set_origin(inp)
        except:
            pass

        dog_list.append(doggy)

    return dog_list

def List_of_breeds(dogs):
    breed_list = []
    for doggy in dogs:
        if doggy.breed_group not in breed_list and doggy.breed_group:
            breed_list.append(doggy.breed_group)
    return breed_list

def search(name,data):
        return list(filter(lambda x:  (x.breed_group) == name  , data))
    

if __name__ == "__main__":
    print()
