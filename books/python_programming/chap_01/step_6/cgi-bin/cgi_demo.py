import cgi

# 解析表单数据
form = cgi.FieldStorage()

print('Content-tpe:text/html\n')
print('<title>Reply Page</title>')
if not 'user' in form:
    print('<h1>Who are you?</h1>')
else:
    print('<h1>Hello <i>%s</i></h1>' % form['user'].value)
