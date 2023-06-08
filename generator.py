import string
import random
from dataclasses import dataclass
import pickle
from typing import List

@dataclass
class Table:
  id: int
  capacity: int
  reservation_code: str
  customer_list: List = None

random.seed(1)
letters = string.ascii_lowercase + string.ascii_uppercase

def create_files(size:int):
  def create_reservation_codes(n:int):
    codes = []
    for _ in range(n):
      size = random.randint(3,5)
      code = "".join([random.choice(letters)+random.choice("0123456789") for _ in range(size)])
      codes.append(code)
    return codes

  def create_names(n:int):
    groups = []
    for i in range(1,n+1):
      group_size = random.randint(1,4)
      group = []
      for j in range(group_size):
        size = random.randint(5,10)
        name = f"Customer{i}{j}, {random.choice(['vegan','non-vegan'])}"
        group.append(name)
      groups.append(group)
    return groups

  def write_file(path:str, data:str):
    with open(path,"w") as f:
      f.write(data)

  reservation_codes = create_reservation_codes(size)
  names = create_names(size)
  data = list(zip(names, reservation_codes))
  reservations = ""
  group_lists = ""
  for group in data:
    people = group[0]
    reservation = group[1]
    reservations += f"{','.join(people)}--{reservation}\n"
    group_lists += '\n'.join(people)+"\n"+reservation+"\n"

  write_file("customer_reservations.txt", group_lists)

  tables = []
  for idx,res_code in enumerate(reservation_codes):
    tables.append(Table(idx,random.randint(1,4),res_code))

  random.shuffle(tables)
  with open("table_data.pickle","wb") as f:
    pickle.dump(tables,f)
    
create_files(100)