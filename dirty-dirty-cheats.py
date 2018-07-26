title = "shake it off"
prepositions = ['cause', 'and', '', '', 'and', '']
nouns = ['players', 'haters', 'baby, I\'m just gonna', 'heartbreakers', 'fakers', 'baby I\'m just gonna']
verbs = ['play', 'hate', 'shake', 'break', 'fake', 'shake']

cursor = 0 

while cursor < len(verbs):
    if (cursor + 1) % 4 is 0:
        print "{}, {}".format(title, title)
    output = [prepositions[cursor]]
    if prepositions[cursor] is not '':
        output.append(' the ')
    output.append(nouns[cursor] + ' gonna ')
    v = verbs[cursor]
    output.append('{}, {}, {}, {}, {}'.format(v, v, v, v, v))
    print ''.join(output)
    cursor += 1

