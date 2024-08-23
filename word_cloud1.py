from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


diretorio = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

#le o arquivo
text = open(path.join(diretorio, 'Divina Comedia.txt')).read()

dante_mask = np.array(Image.open(path.join(diretorio, r'C:\Users\dante\OneDrive\Documentos\5. Estudos\5.8 Python\PythonDSA\Projetos\Word Cloud\dante.jpeg')))

mask = dante_mask.copy()
mask[mask.sum(axis=2) == 0] = 255

pare_palavras = set(STOPWORDS)
pare_palavras.add('said')


wc = WordCloud(
    background_color="white", 
    max_words=5000, 
    mask=dante_mask,
    stopwords=pare_palavras, 
    max_font_size=200, 
    random_state=42
    )

wc.generate(text)

imagem_colors = ImageColorGenerator(dante_mask)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(wc, interpolation="bilinear")
axes[1].imshow(wc.recolor(color_func=imagem_colors), interpolation="bilinear")
axes[2].imshow(dante_mask, cmap=plt.cm.gray, interpolation="bilinear")

for ax in axes:
    ax.set_axis_off()
plt.show()