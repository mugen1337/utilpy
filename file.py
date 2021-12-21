import glob

# pathの一覧をリストで
# https://note.nkmk.me/python-pathlib-iterdir-glob/
file_li = glob.glob("./*.txt")


# int, 改行区切りのファイル，リストに読む
def read(path):
    with open(path) as f:
        li = [int(s.strip()) for s in f.readlines()]

    print(li)
