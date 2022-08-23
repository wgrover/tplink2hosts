import re
import pyperclip as pc

paste = pc.paste()

result = re.findall('\n(.*)\n[-0-9A-F]{17}\n(.*)\n', paste)
for client in result:
    print(f"{client[1]}\t{client[0]}")