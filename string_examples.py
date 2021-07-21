
s1 = "spam\n"
print(s1, len(s1))
s2 = 'spam\n'
print(s2)
print(len(s2))
print(repr(s2))
s3 = """spam\n"""
s4 = '''spam\n'''

print("Guido's the BDFL emeritus of Python")
print('Guido is the "BDFL emeritus" of Python')

print("""Guido's the "BDFL emeritus" of Python""")
print('''Guido's the "BDFL emeritus" of Python''')

s5 = r"spam\n"
print(s5)
print()

actor = "Chris Hemsworth"
a1 = actor.upper()
a2 = actor.lower()
print(a1, a2)
print(a1.upper(), len(a1))
print("wow!".upper())
print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))
actor.lower()
print(actor)
print(actor.find('is'))
print(actor.find("Hem"))
print(actor.find("Liam"))
print(actor.startswith('Chris'))
print(actor.startswith('Liam'))
print(actor.lower().startswith('chris'))
print("Hem" in actor)  # x in y means y contains x
print("Haw" in actor)
print(actor.replace('Chris', 'Liam'))
print(actor.replace('Chris ', ''))
print(actor.replace('wombat', 'mongoose'))
print(actor.find(' Chris'))
print(actor.find('Chris '))

s = "     All my exes live in Texas     "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s = "xyxxyyxxxyyyAll my exes lives in Texasyyyxxxyyxxyxxxxxxxxyyyyyyy"
print("|" + s.lstrip('xy') + "|")
print("|" + s.rstrip('xy') + "|")
print("|" + s.strip('xy') + "|")
print()
















