import cgi, shelve, sys, os

# todo %%(%s)s :我不理解，为什么会有双百分号
# todo %(key)s :传入的是个字典，用这种方式可以获取到字典中key对应的值

shelve_name = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')

form = cgi.FieldStorage()
print('Content-type: text/html')

# 将当前路径改为了包搜索路径，为什么要这样做
sys.path.insert(0, os.getcwd())

reply_html = """
<html>
<head>
    <title>People Input Form</title>
</head>
<body>
    <form method="post" action="people_cgi.py">
        <table>
            <tr>
                <th>key</th>
                <td><input type="text" name="key" value="%(key)s"></td>
            </tr>
            $ROWS$
        </table>
        <p>
            <input type="submit" value="Fetch" name="action">
            <input type="submit" value="Update" name="action">
    </form>
</body>
</html>
"""

row_html = '<tr><th>%s</th><td><input type="text" name=%s value="%%(%s)s"></td></tr>'
rows_html = ''

for fieldname in fieldnames:
    rows_html += (row_html % ((fieldname,) * 3))
reply_html = reply_html.replace('$ROWS$', rows_html)


def htmlize(adict):
    new = adict.copy()
    for field in fieldnames:
        value = new[field]
        # new[field] = cgi.escape(repr(value))
        new[field] = repr(value)
    return new


def fetchRecord(db, form):
    try:
        key = form['key'].value
        record = db[key]
        fields = record.__dict__
        fields['key'] = key
    except:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing or invalid key!'
    return fields


def updateRecord(db, form):
    if not 'key' in form:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing key input!'
    else:
        key = form['key'].value
        if key in db:
            record = db[key]
        else:
            from books.python_programming.chap_01.step_3.person_alternative import Person
            record = Person(name='?', age='?')

        for field in fieldnames:
            setattr(record, field, eval(form[field].value))
        db[key] = record
        fields = record.__dict__
        fields['key'] = key
    return fields


db = shelve.open(shelve_name)
action = form['action'].value if 'action' in form else None
if action == 'Fetch':
    fields = fetchRecord(db, form)
elif action == 'Update':
    fields = updateRecord(db, form)
else:
    fields = dict.fromkeys(fieldnames, '?')
    fields['key'] = 'Misstion or invalid action!'
db.close()
print(reply_html % htmlize(fields))
