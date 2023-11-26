import os
import platform

import platform

my_os = platform.system()

class link :
    class linux:
        github = "https://github.com/Fuxeur/fire-shell-en-all.git"
    class win :
        github = "https://github.com/Fuxeur/fire-shell-en-all.git"
    class mac:
        github = "https://github.com/Fuxeur/fire-shell-en-all.git"
    class all:
        github = "https://github.com/Fuxeur/fire-shell-en-all.git"


print("installing package..")

os.system("pip install tqdm")

from tqdm import tqdm

req = ["colorama","socket"]
for i in tqdm(range(len(req))):
    os.system("pip install " + req[i])

lang = ["en"]

if len(lang) == 1:
    print("installing language : " + lang)
    print("and for os : " + my_os)
    for i in tqdm(range(1)):
        os.system("git clone " + link.all.github)