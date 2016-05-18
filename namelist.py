
'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names,
which should be separated by an ampersand.

Example:
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''

Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
'''


def namelist(names):
    names_list = ''
    list_length = len(names)
    if list_length == 0:
        return names_list
    if list_length == 1:
        return names_list + names[0]['name']
    counter = 0
    while list_length - counter > 2:
        names_list += names[counter]['name'] + ', '
        counter += 1
    names_list += names[counter]['name'] + ' & ' + names[counter+1]['name']
    return names_list

# more beautiful solution (pythonic way)
def namelist2(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''