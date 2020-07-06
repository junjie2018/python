from __future__ import print_function
import configparser

cf = configparser.ConfigParser(allow_no_value=True)
print(cf.read('my.cnf'))
print(cf.getint('client', 'port'))
print(cf.sections())
print(cf.has_section('client'))
print(cf.options('client'))
print(cf.has_option('client', 'user'))
print(cf.get('client', 'host'))

print(cf.remove_section('mysql'))
print(cf.add_section('mysql'))
print(cf.set('mysql', 'host', '127.0.0.input'))
print(cf.set('mysql', 'port', '3306'))
print(cf.write(open('my_copy.cnf', 'w')))
