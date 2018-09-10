import pymysql
from collections import Iterable


def get_table_data_list(table, database, selected_fields=None):

    data_list = []
    
    with pymysql.connect(**database) as cursor:

            all_fields = []
            cursor.execute("DESC {}".format(table))
            for info in cursor:
                field = info[0]
                all_fields.append(field)

            if selected_fields:
                if isinstance(selected_fields, str):
                    selected_fields = [selected_fields, ]
                
                if isinstance(selected_fields, Iterable):
                    for f in selected_fields:
                        if not f in all_fields:
                            return False, "Not all selected fields are available"
            else:
                selected_fields = all_fields

            sql = ",".join(selected_fields)
            sql = "SELECT " + sql + " FROM " + table
            cursor.execute(sql)

            for row in cursor:
                if len(row) == len(selected_fields):
                    item = {}
                    for field_index, field_value in enumerate(row):
                        item[selected_fields[field_index]] = field_value
                    data_list.append(item)

    return data_list


if __name__ == '__main__':

    database = {
        'host': 'localhost',
        'user': 'root',
        'db': 'test',
        'table': 'hellotest'
    }

    table = database.pop('table')

    data_list = get_table_data_list(table=table, database=database, selected_fields='testid')
    print(data_list)
