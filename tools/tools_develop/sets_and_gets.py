for line in open('input.txt'):
    line = line.strip()
    if not line:
        continue

    strs = line.split()
    print('openCardDTO.set%s("");' % ("%s%s" % (strs[2][0].upper(), strs[2][1:-1])))
