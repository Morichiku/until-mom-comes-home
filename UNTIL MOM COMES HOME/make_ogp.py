# make_ogp.py
# 実行すると share0.html 〜 share10.html の11ファイルを同じフォルダに自動生成します

# ★公開先のフォルダURL（末尾に / をつけてください）
BASE_URL = "https://morichiku.github.io/"
# ★結果イラストが置いてあるパスと拡張子（例: "images/end0.jpg" なら DIR="images/", EXT=".jpg"）
IMG_DIR = "images/"
IMG_EXT = ".jpg"

for i in range(11):
    title = (
        f"UNTIL MOM COMES HOME — ママが帰るまで — ({i}/10)"
        if i < 10
        else "UNTIL MOM COMES HOME — ママが帰るまで — (10/10 CLEAR!)"
    )
    desc = (
        "雷とスマホライトで気配を探りながら、ママに10通のLINEを送って助けを呼べ。"
    )
    img_url = f"{BASE_URL}{IMG_DIR}end{i}{IMG_EXT}"

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<meta name="twitter:card" content="summary_large_image">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{img_url}">
<meta property="og:type" content="website">
<meta http-equiv="refresh" content="0; url=./index.html">
<script>location.replace("./index.html");</script>
</head>
<body style="background:#000015;color:#fff;font-family:sans-serif;text-align:center;padding-top:40vh;">
  <p>ゲーム画面へ移動中... <a href="./index.html" style="color:#63b3ed;">移動しない場合はこちら</a></p>
</body>
</html>
"""
    with open(f"share{i}.html", "w", encoding="utf-8") as f:
        f.write(html)

print("✓ share0.html 〜 share10.html の全11ファイルを生成しました！")