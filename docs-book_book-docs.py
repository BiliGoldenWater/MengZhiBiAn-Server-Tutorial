import os

if os.path.exists(".\\_book"):
    os.system("rename _book docs")
elif os.path.exists(".\\docs"):
    os.system("rename docs _book")