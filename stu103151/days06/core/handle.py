import db.sql_api as sql
def select_all(table_name):
    '''
    根据表查询所有的商品信息
    :param table_name:
    :return: 商品信息
    '''
    func = sql.select_all(table_name)
    return func
def select_equipment(table_name,id):
    '''
    根据表和商品ID查询该商品名称
    :param table_name:
    :param id:
    :return:商品名称
    '''
    func = sql.select_equipment(table_name,id)
    return  func
def select_equipment_power(table_name,column):
    '''
    根据表和列查询power
    :param table_name:
    :param column:
    :return: power
    '''
    func = sql.select_equipment_power(table_name,column)
    return  func



