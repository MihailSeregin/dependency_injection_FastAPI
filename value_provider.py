class ValueProvider:
    def __init__(self, quantity: int):
        self.quantity = quantity
        self.potential_users_db = [[1,5,2,-3,0,11] for i in range(self.quantity)]

    def provide_values(self, user_id):
        return self.potential_users_db[user_id]