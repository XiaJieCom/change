import db.sql_api as sql
def select_all(table_name):
    func = sql.select_all(table_name)
    return func
def select_equipment(table_name,id):
    func = sql.select_equipment(table_name,id)
    return  func
def select_equipment_power(table_name,column):
    func = sql.select_equipment_power(table_name,column)
    return  func


