import os

input_dir = r"C:\Users\Junjie\Desktop\project\mmp-brand-member2\brand-member-api\src\test\java\test\domain\entity"
output_dir = r"C:\Users\Junjie\Desktop\data"

for input_file_name in os.listdir(input_dir):
    old_file_name, ext_name = os.path.splitext(input_file_name)
    new_file_name = old_file_name[3:]
    output_file_name = new_file_name + ext_name

    with open(os.path.join(output_dir, output_file_name), 'w', encoding='utf8') as output_os:
        for line in open(os.path.join(input_dir, input_file_name), 'r', encoding='utf8'):
            output_os.write(line.replace(old_file_name, new_file_name))
