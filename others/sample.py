import re
f = open('sample.txt', 'rt')
source = f.read().strip().replace('\t', '')

def find_tag(tag_name, class_, source):
    p = re.compile(r'<{tag_name} class="{class_name}".*?>.*?</{tag_name}>'.format(
        tag_name=tag_name,
        class_name=class_))
    return re.findall(p, source)


# <td class="title">...</td>에 해당하는 내용들
p = re.compile(r'<td class="title".*?>.*?</td>', re.DOTALL)

result = re.findall(p, source)
for index, item in enumerate(result):
    print('== index %s ==' % index)
    
    # >와 <사이의 공백을 모두 없앰
    cur_strip_item = re.sub(r'>\s*?<', r'><', item, flags=re.DOTALL)
    #print(cur_strip_item)

    # a태그 내부의 내용을 출력
    cur_title = re.sub(r'.*?<a.*?>(.*?)</a>.*', r'\g<1>', cur_strip_item)
    print(cur_title)

print('Total items:', len(result))

