"""実践：画像を一括リサイズ　※準備が面倒なのでソースタイピングのみ

import os
from PIL import Image

fnames = os.listdir("potho")

for fname in fnames:
    if "cat" in fname:
        fpath = os.path.join("photo",fname)
        img = Image.open(fpath)
        img.thumbnail((150,150))
        img.save(fpath)

"""