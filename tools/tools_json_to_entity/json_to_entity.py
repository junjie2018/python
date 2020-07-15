import json

outer_class = []
inner_class = {}


class Field:
    def __init__(self, field_tame, field_type, is_list=False):
        self.fieldName = field_tame
        self.fieldType = field_type
        self.is_list = is_list


def outer_dispose(data_element):
    for key in data_element:
        if isinstance(data_element[key], list):
            # 暂时不考虑list嵌套的问题
            if len(data_element[key]) > 0:
                if isinstance(data_element[key][0], dict):
                    outer_class.append(Field(key, key, True))

                    # 处理内部类型
                    inner_class[key] = []
                    inner_dispose(key, data_element[key][0])
                else:
                    outer_class.append(Field(key, 'string', True))
            else:
                outer_class.append(Field(key, 'string', True))
        elif isinstance(data_element[key], dict):
            outer_class.append(Field(key, key))

            # 处理内部类型
            inner_class[key] = []
            inner_dispose(key, data_element[key])
        else:
            outer_class.append(Field(key, 'string'))


def inner_dispose(class_name, element):
    for key in element:
        if isinstance(element[key], list):
            if len(element[key]) > 0:
                if isinstance(element[key][0], dict):
                    inner_class[class_name].append(Field(key, key, True))

                    # 处理内部类型
                    inner_class[key] = []
                    inner_dispose(key, element[key][0])
                else:
                    inner_class[class_name].append(Field(key, 'string', True))
            else:
                inner_class[class_name].append(Field(key, 'string', True))
        elif isinstance(element[key], dict):
            inner_class[class_name].append(Field(key, key))

            # 处理内部类型
            inner_class[key] = []
            inner_dispose(key, element[key])
        else:
            inner_class[class_name].append(Field(key, 'string'))


def generateLine(prefix, field):
    result = ''
    if field.is_list:
        result += '%spublic List<%s> %s;\n' % (prefix, field.fieldType.capitalize(), field.fieldName)
    else:
        result += '%spublic %s %s;\n' % (prefix, field.fieldType.capitalize(), field.fieldName)
    return result


def generateOuterClass(outer_class, inner_class_content):
    result = ''
    result += '@Data\n'
    result += '@NoArgsConstructor\n'
    result += '@AllArgsConstructor\n'
    result += 'public class %s {\n' % 'Temp'

    for field in outer_class:
        result += generateLine('\t', field)

    result += '\n\n'
    result += inner_class_content

    result += '}\n'

    return result


def generateInnerClass(inner_class):
    result = ''
    for class_name in inner_class:
        result += '\t@Data\n'
        result += '\t@NoArgsConstructor\n'
        result += '\t@AllArgsConstructor\n'
        result += '\tpublic static class %s {\n' % class_name.capitalize()

        for field in inner_class[class_name]:
            result += generateLine('\t\t', field)
        result += '\t}\n\n'
    return result


if __name__ == '__main__':
    with open('input.json', encoding='utf8') as file:
        root_element = json.load(file)
        data_element = root_element['data']
        if isinstance(data_element, list):
            if len(data_element) > 0:
                outer_dispose(data_element[0])
        elif isinstance(data_element, dict):
            outer_dispose(data_element)
        else:
            raise Exception()

    inner_class_content = generateInnerClass(inner_class)
    print(generateOuterClass(outer_class, inner_class_content))
