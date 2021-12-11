import requests


class GetNameFromAPI:
    def __init__(self, quantity=None):
        self.__url = "http://gerador-nomes.herokuapp.com/"
        self.__name_ep = "nomes"
        self.__lname_ep = "apelidos"
        self.__quantity = 10 if quantity is None else quantity

    def get_name_list(self):
        names_data = [self.__get_data("name"), self.__get_data("last_name")]

        return self.__merge_name(names_data)

    def __get_data(self, data_type):
        complete_url = self.__url
        document: requests.Response

        if data_type == "name":
            complete_url += f"{self.__name_ep}/{self.__quantity}"
        elif data_type == "last_name":
            complete_url += f"{self.__lname_ep}/{self.__quantity}"
        else:
            raise ValueError(f"GetNameFromAPI: data type is unkown: data_type: {data_type}")

        try:
            document = requests.get(complete_url)
            if document.status_code == 200:
                return document.json()
            else:
                raise Exception(f"GetNameFromAPI error during API communication fetch. "
                                f"Error code: {document.status_code}")
        except Exception as e:
            print("GetNameFromAPI error during API communication fetch.", e)

    def __merge_name(self, names_list):
        names = []
        counter = 0
        while counter < self.__quantity:
            full_name = f"{names_list[0][counter]} {names_list[1][counter]}"
            names.append(full_name)
            counter += 1
        return names





