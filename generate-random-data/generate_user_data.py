
from names import GetNameFromAPI
from cpf import RandomCPF


class GenerateUserData:

    def __init__(self, quantity=None):
        self.__quantity = 10 if quantity is None else quantity
        self.__names_list = GetNameFromAPI(self.__quantity)
        self.__cpf_list = RandomCPF(self.__quantity)

    def get_user_data(self):
        random_data = []

        names = self.__names_list.get_name_list()
        cpfs = self.__cpf_list.get_cpf_list()

        for i in range(0, self.__quantity):
            user_data = {'cpf': cpfs[i], 'name': names[i]}
            random_data.append(user_data)

        return random_data


