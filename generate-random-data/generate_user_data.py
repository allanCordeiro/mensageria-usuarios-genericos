from names import GetNameFromAPI
from cpf import RandomCPF


def generate_user_data(quantity=None):
    data_qty = 10 if quantity is None else quantity
    names_list = GetNameFromAPI(data_qty)
    cpf_list = RandomCPF(data_qty)
    random_data = []

    names = names_list.get_name_list()
    cpfs = cpf_list.get_cpf_list()

    for i in range(0, data_qty):
        user_data = {'cpf': cpfs[i], 'name': names[i]}
        random_data.append(user_data)

    return random_data


if __name__ == "__main__":
    user_data = generate_user_data(2)
    print(user_data)