import random
import names

movie=["fast x","avengers","endgame","infinity","2012","age of ultron","omg"]

data= dict()

for i in range(5):
    director_name=names.get_full_name()
    actor_name=names.get_full_name()
    r_date=str(random.randint(1,31)),str(random.randint(1,12)),str(random.randint(1999,2023))

    name={'director':director_name,'actor':actor_name,'release':r_date}
    data[str(director_name)]=name

for i in data:
    print(data[i])

