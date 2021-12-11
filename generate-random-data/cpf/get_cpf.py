import random


class RandomCPF:
    def __init__(self, quantity=None):
        self.__quantity = 0 if quantity is None else quantity

    def get_cpf_list(self):
        cpf_list = []
        for i in range(0, self.__quantity):
            random_number = self._get_random_seq()
            # random_number = [3, 2, 8, 8, 3, 1, 6, 8, 8]
            first_digit = self._get_verification_digit(random_number, "J")
            final_digit = self._get_verification_digit(first_digit, "K")
            cpf_list.append(self._prettify(final_digit))

        return cpf_list

    @staticmethod
    def _get_random_seq():
        randomized = []
        for i in range(0, 9):
            randomized.append(random.randint(0, 9))
        return randomized

    @staticmethod
    def _get_verification_digit(random_set: list, digit_pos: str):
        data = random_set
        total = 0
        verified = 0
        starts_with = 10 if digit_pos.upper() == "J" else 11
        for number in data:
            total += number * starts_with
            starts_with -= 1
            if starts_with < 2:
                break

        verified = total % 11
        if verified == 0 or verified == 1:
            data.append(0)
        else:
            verified = 11 - verified
            data.append(verified)
        return data

    def _prettify(self, number_list):
        masked_cpf = f"{self._slice_to_string(number_list[0:3])}." \
                     f"{self._slice_to_string(number_list[3:6])}." \
                     f"{self._slice_to_string(number_list[6:9])}-" \
                     f"{self._slice_to_string(number_list[9:])}"
        return masked_cpf

    @staticmethod
    def _slice_to_string(sliced_number: list):
        string_number = ""
        for number in sliced_number:
            string_number += str(number)
        return string_number


if __name__ == "__main__":
    cpf = RandomCPF(10)
    print(cpf.get_cpf_list())

