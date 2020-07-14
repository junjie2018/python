import os


def get_field_name(field):
    return field['name']


def get_field_type(field):
    if field['type'] == 'varchar':
        return 'varchar({})'.format(field['length'])
    elif field['type'] == 'int':
        # 判断常数
        if int(field['length']) > 4:
            return 'bigint({}) unsigned'.format(field['length'])
        else:
            return 'tinyint({}) unsigned'.format(field['length'])
    elif field['type'] == 'datetime':
        return 'datetime'
    elif field['type'] == 'tinyint':
        return 'tinyint({}) unsigned'.format(field['length'])
    elif field['type'] == 'bigint':
        return 'bigint({}) unsigned'.format(field['length'])
    else:
        return '############# WRONG #############'


def get_field_is_not_blank(field):
    if field['is_not_blank'] == '是':
        return 'not null'
    else:
        return ''


def get_field_is_create_time(field):
    if field['name'] == 'create_at':
        return 'default CURRENT_TIMESTAMP'
    else:
        return ''


def get_field_is_update_time(field):
    if field['name'] == 'update_at':
        return 'default CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'
    else:
        return ''


def get_field_comment(field):
    return "comment '{}'".format(field['comment'])


def get_field_is_auto_increment(field):
    if field['is_primary'] == 'PK':
        return 'AUTO_INCREMENT'
    else:
        return ''


def get_primary(field):
    if field['is_primary'] == 'PK':
        return '\tprimary key ({})'.format(field['name'])
    else:
        return ''


def main():
    for filename in os.listdir('inputs'):
        line_count = 0
        table_name = ''
        table_comment = ''
        primary = ''
        content = ''
        with open(os.path.join(os.getcwd(), 'inputs', filename), encoding='utf-8') as file:
            for line in file.readlines():
                segments = line.split('\t')

                if line_count < 2:
                    if line_count == 0:
                        table_name = segments[3]
                        table_comment = segments[1]
                        # print(table_comment)
                        # print(table_name)

                    line_count += 1
                    continue

                field = {
                    "comment": segments[1],
                    "name": segments[2],
                    "type": segments[3],
                    "length": segments[4],
                    "is_primary": segments[5],
                    "is_not_blank": segments[6]
                }

                content += "\t{field_name} {field_type} {field_is_not_blank} {field_is_auto_increment} {field_is_create_time} {field_is_update_time} {field_comment} ,\n".format(
                    field_name=get_field_name(field),
                    field_type=get_field_type(field),
                    field_is_not_blank=get_field_is_not_blank(field),
                    field_is_auto_increment=get_field_is_auto_increment(field),
                    field_is_create_time=get_field_is_create_time(field),
                    field_is_update_time=get_field_is_update_time(field),
                    field_comment=get_field_comment(field)
                )
                primary += get_primary(field)

            if primary == '':
                # 如果不包含主键，则取出最后的一个逗号和换行符，并还原换行符
                content = content[:-2]
                content += '\n'
            else:
                content += primary + '\n'

            print("drop table if exists `{}`;".format(table_name, table_name))
            print("create table {} (\n{});\nalter table {} comment '{}';".format(table_name, content, table_name,
                                                                                 table_comment))


if __name__ == '__main__':
    main()
