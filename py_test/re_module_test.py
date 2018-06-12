import re
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
m = pattern.match('hello world Wide Web')

print(m)