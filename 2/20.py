import json

with open('jawiki-country.json') as jawiki:
    with open('20.txt', 'w') as output:
        for line in jawiki:
            line_dict = json.loads(line.strip('\n'))
            if line_dict['title'] == u'イギリス':
                print(line_dict['text'])
                output.write(line_dict['text'] + '\n')
