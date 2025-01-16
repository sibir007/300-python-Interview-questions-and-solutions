import re

match_header = r'(^\d+\. )(.*)'
match_whitespace = r'^\s*$'
match_print = r'print’(.*)’(.*)'

with open('350interview.txt', 'rt', encoding='utf-8') as f:
    while line:= f.readline():
        if m:=re.match(match_print, line):
            print('print(line): ' + line)
            print('print(m.group()): ' + m.group())
            print('print(m.group(0)): ' + m.group(0))
            print('print(m.group(1)): ' + m.group(1))
            print('print(m.group(2)): ' + m.group(2))
            new_line = line.replace(m.group(0), f"print('{m.group(1)}', {m.group(2)})")
            print('print(new_line): ' + new_line)
            
            
        # if(m:=re.match(match_whitespace, line)):
    # with open('350interview_cor.txt', 'wt', encoding='utf-8') as f2:
    #     counter = 1
            #     continue
        
            # if m:=re.match(match_header, line):
            #     f2.write(f'\n### {str(counter)}. {m.group(2).strip()}\n\n')
            #     # print(m.group(2))
            #     # print(f'### {str(counter)}. {m.group(2).strip()}')
            #     counter += 1
            #     continue
            # f2.write(line)
            

        
        