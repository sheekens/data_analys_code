# data_analys_code
## Markdown readable view in VScode
```
В VSCode: Ctrl+P -> в всплывшем окне > Markdown. Open preview on a side.
```

[Шпаргалка по оформлению](https://github.com/sandino/Markdown-Cheatsheet?ysclid=ljlp840fsr885829786)

### последовательность заливки из VSCode в Git

```bash
git status
git add 'path_to_file' #git add -A  - add all files
git commit -m 'commentarii'
git push
```

### запуск виртуального окружения cv

```
python3 C:\Users\User\venvs\cv\Scripts\Activate.ps1
```

### IMG parametres:

img.shape = height, width, channels
channels = BGR #NOT RGB

### cv2 IMG read, write

cv2.imread(path)
cv2.imwrite(path, file)