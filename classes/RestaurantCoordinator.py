from NonVeganCustomer import NonVeganCustomer
from VeganCustomer import VeganCustomer
import pickle
from Table import Table

class RestaurantCoordinator():
    customers_list = []

    def __init__(self) -> None:
        pass

    def deserialization(self):
        file = open('table_data.pickle', 'rb')
        tables = pickle.load(file)
        return tables

    def return_custumer_by_type(self, arr):
        #arr will have two positions, the second one is the type
        if 'non-vegan' not in arr:
            newVeganCustomer = VeganCustomer()
            return  newVeganCustomer
        else:
            newNonVeganCustomer = NonVeganCustomer()
            return newNonVeganCustomer

    def create_customer(self):
        file = open('customer_reservations.txt', 'r', encoding='utf-8').read()
        lines_arr = file.splitlines()

        tables = self.deserialization()

        customers = []

        for i in range(len(lines_arr)):
            #Check for table code
            if 'Customer' not in lines_arr[i]: 
                for j in range(len(tables)):
                    if tables[j].reservation_code == lines_arr[i]:
                        if tables[j].capacity > len(customers):
                            print('There are more customers than tables')
                        else:
                            tables[j].customer_list = customers
                #Saving data
                customers.append(lines_arr[i])
                self.customers_list.append(customers)
                #reinitiate customers
                customers = []
            else:
                new_customer = self.return_custumer_by_type(lines_arr[i])
                customers.append(new_customer)
        
        for i in range(len(tables)):
            print(repr(tables[i].customer_list))