from value_provider import ValueProvider

class SorterValues:
    def __init__(self, init_param):
        self.init_param = init_param

    def sort_values(self, lst: list[int]):
        lst.sort()
        return lst


class Substractor:
    def __init__(self, substractor_digit):
        self.substractor_digit = substractor_digit

    def substract(self, lst: list[int]):
        return [(i - self.substractor_digit) for i in lst]


class Pipeline:
    def __init__(self, value_provider: ValueProvider, sorter_values: SorterValues, substractor: Substractor):
        self.sorter_values = sorter_values
        self.substractor = substractor
        self.value_provider = value_provider

    def recommend(self,user_id):
        
        potential_partners = self.value_provider.provide_values(user_id)
        potential_partners = self.substractor.substract(potential_partners)
        potential_partners = self.sorter_values.sort_values(potential_partners)

        return potential_partners
