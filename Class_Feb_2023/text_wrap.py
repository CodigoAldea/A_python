import textwrap

s = '''textwrap.wrap(text, width=70, *, 
initial_indent='', subsequent_indent='', 
expand_tabs=True, replace_whitespace=True, 
fix_sentence_endings=False, break_long_words=True, 
drop_whitespace=True, break_on_hyphens=True, tabsize=8, 
max_lines=None, placeholder=' [...]')'''

print(textwrap.fill(s, width=100))