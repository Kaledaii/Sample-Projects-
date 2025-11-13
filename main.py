with open('story.txt', 'r') as f:
    story = f.read()
    print("Before:\n",story)
start=-1

words=set()
for i,char in enumerate(story):
    if char == '<':
        start=i
    if (char == '>')and (start!=-1):
        w= story[start:i+1]
        words.add(w)
        start=-1    
print(words)
for w in words:
    replace=input(f'Enter {w}:')
    story=story.replace(w,replace)
print("After:\n",story)