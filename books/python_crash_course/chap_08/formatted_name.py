def get_formattd_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name+' '+last_name
    return full_name


musician = get_formattd_name('jimi', 'hendrix')
print(musician)


def get_formattd_name2(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name+' '+middle_name+' '+last_name
    else:
        full_name = first_name+' '+last_name
    return full_name.title()

musician = get_formattd_name2('jimi', 'hendrix')
print(musician)
musician = get_formattd_name2('jimi', 'hendrix','lee')
print(musician)
