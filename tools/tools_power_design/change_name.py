import xml.dom.minidom as xmldom


def main():
    filename = 'PhysicalDataModel_1.pdm'

    dom_obj = xmldom.parse(filename)
    document = dom_obj.documentElement

    columns = document.getElementsByTagName('c:Columns')

    for column in columns:
        sub_columns = column.getElementsByTagName('o:Column')
        for sub_column in sub_columns:
            name = sub_column.getElementsByTagName('a:Name')[0]
            comment = sub_column.getElementsByTagName('a:Comment')[0]

            name.firstChild.data = comment.firstChild.data

    with open('tmp.pdm', 'w') as file:
        dom_obj.writexml(file)


if __name__ == '__main__':
    main()
