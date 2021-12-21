import numpy as np
import matplotlib.pyplot as plt

# x=0とか y=0のところに線を引く．
# gridとかでx=0とかy=0に意味がある時に重宝する
# zorder で　複数の線などとの表示順をコントロール，大きい方が手前にくる．
# alpha で透明度を調節
plt.axhline(y=0, xmin=-2.2, xmax=2.2, color="black", alpha=0.2, zorder=1)
plt.axvline(x=0, ymin=-2.2, ymax=2.2, color="black", alpha=0.2, zorder=2)
