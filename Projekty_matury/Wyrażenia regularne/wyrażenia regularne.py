import re
wzor = r"banan"
tekst = r"jabłkobanantruskawkibananoweorzechy"
tekst2 = r"bananjabłkobanantruskawkibananoweorzechy"


if re.match(wzor, tekst):
    print("Tekst1 zaczyna się od wzoru")
else:
    print("Tekst1 nie zaczyna się od wzoru")

if re.match(wzor, tekst2):
    print("Tekst2 zaczyna się od wzoru")


obiekt = re.search(wzor, tekst)

print(obiekt.group())
print(obiekt.start())
print(obiekt.end())
print(obiekt.span())

print(re.findall(wzor, tekst))

print(len(re.findall(wzor, tekst)))

print(re.findall(r'.*' + wzor + r'.*', tekst))



    


