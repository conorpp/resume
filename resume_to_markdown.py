#!/usr/bin/env python

import json, sys, re

if len(sys.argv) != 2:
    print 'usage: %s <resume.json>' % sys.argv[0]
    sys.exit(1)

text = open(sys.argv[1],'r').read()
text = re.sub(r'<[^>]+>','', text)
obj = json.loads(text)

print '**'+ obj['name'] +'**'
print
print
print
print '**Website**: '+obj['website']+''
print
print '**'+ obj['contact'] +'**', '(pgp key: '+obj['fingerprint']+')'
print
print '**207 659 5209**'
print
print '**'+ obj['location'] +'**'
print
print
print
print
print

for b in obj['subjects']:
    print b['name']
    print '========'
    print 

    for i in b['items']:
        if i.get('hide',False): continue

        if i['type'] == 'plain':
            print '*', i['content']

        elif i['type'] == 'label':
            print '*', '**'+i['name']+'**'+':', i['content']

        elif i['type']=='list':
            print '*', i['name']
            print 

            for li in i['content']:
                print '    *',li['content']
        else:
            raise RuntimeError('invalid type '+i['type'])

        print

