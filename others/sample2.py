import re

f = open('sample.txt', 'rt')
source = f.read().strip().replace(r'\t', '')

result = re.findall(r'<td class="title">.*?</td>', source)
print(result)

