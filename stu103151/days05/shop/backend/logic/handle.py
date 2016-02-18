from backend.db import sql_api


def select_all():
    func = sql_api.select_all()
    return func
def select_price(id):
    func = sql_api.select_price(id)
    return func



'''
def update_amount(name,new_amount):
    func = sql_api.update(name,new_amount)
    return func
'''