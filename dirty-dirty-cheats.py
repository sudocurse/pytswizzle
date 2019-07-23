title = "shake it off"
prepositions = ['cause', 'and', '', '', 'and', '']
nouns = ['players', 'haters', 'baby, I\'m just gonna', 'heartbreakers', 'fakers', 'baby I\'m just']
verbs = ['play', 'hate', 'shake', 'break', 'fake', 'shake']

for cursor in range(0, len(verbs)):
    output = [prepositions[cursor]]
    if prepositions[cursor] is not '':
        output.append(' the ')
    output.append(nouns[cursor] + ' gonna ')
    v = verbs[cursor]
    output.append('{}, {}, {}, {}, {}'.format(v, v, v, v, v))
    print ''.join(output)
    if v is 'shake':
        print "{}, {}".format(title, title)
    cursor += 1

