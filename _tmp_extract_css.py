import re
p = r'C:/Users/benma/ariadnes-thread-os/index.html'
t = open(p, encoding='utf-8').read()
# find line 40 block
idx = t.find('.content-view{')
chunk = t[idx:idx+6000]
for pat in ['content-split', 'content-left', 'doc-list', 'doc-item', 'doc-title', 'doc-badge', 'doc-time']:
    for m in re.finditer(r'\.[\w-]*' + pat.replace('-', r'\-') + r'[^{]*\{[^}]+\}', chunk):
        print('---', m.group(0)[:500])
        print()