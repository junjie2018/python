import os


def get_field_name(field):
    return field['name']


def get_field_is_auto_increment(field):
    if field['is_primary'] == 'PK':
        return 'AUTO_INCREMENT'
    else:
        return ''


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


def get_primary(field):
    if field['is_primary'] == 'PK':
        return '\tprimary key ({})'.format(field['name'])
    else:
        return ''


def get_content(field):
    return "\t{field_name} {field_type} {field_is_not_blank} {field_is_auto_increment} {field_is_create_time} {field_is_update_time} {field_comment} ,\n".format(
        field_name=get_field_name(field),
        field_type=get_field_type(field),
        field_is_not_blank=get_field_is_not_blank(field),
        field_is_auto_increment=get_field_is_auto_increment(field),
        field_is_create_time=get_field_is_create_time(field),
        field_is_update_time=get_field_is_update_time(field),
        field_comment=get_field_comment(field)
    )


def main():
    for filename in os.listdir('inputs'):
        line_count = 0
        table_name = ''
        table_comment = ''
        primary = ''
        content = ''

        special_fields = {'brand_id', 'brand_code', 'channel_id', 'channel_code', 'channel_app_id', 'open_app_id'}
        with open(os.path.join(os.getcwd(), 'inputs', filename), encoding='utf-8') as file:
            for line in file.readlines():
                line_count += 1
                segments = line.split('\t')

                if line_count < 3:
                    if line_count == 1:
                        table_name = segments[3]
                        table_comment = segments[1]
                    continue

                if line_count == 4:
                    # 在这个地方插入5行
                    comments = ['品牌Id', '品牌code', '渠道Id', '渠道code', '渠道应用Id', '对外渠道应用Id']
                    nemes = ['brand_id', 'brand_code', 'channel_id', 'channel_code', 'channel_app_id', 'open_app_id']
                    types = ['int', 'varchar', 'int', 'varchar', 'int', 'varchar']
                    lengths = ['11', '32', '11', '32', '11', '32']

                    for idx in range(6):
                        field = {"comment": comments[idx],
                                 "name": nemes[idx],
                                 "type": types[idx],
                                 "length": lengths[idx],
                                 "is_primary": "否",
                                 "is_not_blank": "是"}
                        content += get_content(field)

                field = {
                    "comment": segments[1],
                    "name": segments[2],
                    "type": segments[3],
                    "length": segments[4],
                    "is_primary": segments[5],
                    "is_not_blank": segments[6]
                }

                # 检测当前行是否为主键
                primary += get_primary(field)
                if line_count == 3 and field['name'] in special_fields:
                    special_fields.remove(field['name'])
                    continue

                if field['name'] in special_fields:
                    continue

                content += get_content(field)

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
