import re

match_header = r'(^\d+\. )(.*)'
match_whitespace = r'^\s*$'
match_print = r'print’(.*)’(.*)'


with open('350interview.txt', 'rt', encoding='utf-8') as f:
    with open('350interview_cor.txt', 'wt', encoding='utf-8') as f2:
        counter = 1
        while line:= f.readline():
            
            if(m:=re.match(match_whitespace, line)):
                continue
            if (m:=re.match(match_print, line)):
                line = line.replace(m.group(0), f'print("{m.group(1)}", {m.group(2)})')
            if m:=re.match(match_header, line):
                f2.write(f'\n### {str(counter)}. {m.group(2).strip()}\n\n')
                # print(m.group(2))
                # print(f'### {str(counter)}. {m.group(2).strip()}')
                counter += 1
                continue
            f2.write(line)
            

        
        