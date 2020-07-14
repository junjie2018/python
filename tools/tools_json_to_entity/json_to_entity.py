import json

outer_class = []
inner_class = []


def recursion_dispose_map(josn_map):
    for key in josn_map:
        print(key)
        if isinstance(josn_map[key], map):
            recursion_dispose_map(josn_map[key])


def main():
    with open('input.json', encoding='utf8') as file:
        root_element = json.load(file)
        data_element = root_element['data']



if __name__ == '__main__':
    main()
