import re

obj = re.match('^(?:H)(?P<first>e)llo .*(Wor(ld|dl))+.*$', 'Hello Wordl WorldWordl')

if obj:
    print("Dopasowano!")
    print(obj.group())
    print(obj.group(1))
    print(obj.group(2))
    print(obj.group(3))
    print(obj.group('first'))
    print(obj.groups())
else:
    print("Nie dopasowano!")

print('\n')

if re.match('([A-Za-z0-9]+|[A-Za-z0-9]+[A-Za-z0-9-\.]*[A-Za-z0-9]+)'
            '@([A-Za-z0-9]+|[A-Za-z0-9]+[A-Za-z0-9-\.]?[A-Za-z0-9]+)'
            '\.([A-Za-z0-9]+|[A-Za-z0-9]+[A-Za-z0-9-\.]?[A-Za-z0-9]+)', 'a-a@p-a.l-a'):
    print("Poprawny email :)")
else:
    print("Niepoprawny email, popraw!")