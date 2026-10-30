# make_ogp.py（Xクローラー対策済み）

# ★実際の公開URL（末尾に必ず / をつける）
BASE_URL = "https://morichiku.github.io/until-mom-comes-home/"

# ★実際の結果画像の拡張子（".png" または ".jpg"）
IMG_DIR = "images/"
IMG_EXT = ".png" 

for i in range(11):
    if i < 10:
        title = f"UNTIL MOM COMES HOME — ママが帰るまで — ({i}/10)"
    else:
        title = "UNTIL MOM COMES HOME — ママが帰るまで — (10/10 CLEAR!)"
    
    desc = "雷とスマホライトで気配を探りながら、ママに10通のLINEを送って助けを呼べ。"
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
<meta property="og:url" content="{BASE_URL}share{i}.html">
<meta property="og:type" content="website">
<script>location.replace("./index.html");</script>
</head>
<body style="background:#000015;color:#fff;font-family:sans-serif;text-align:center;padding-top:40vh;">
  <p>ゲーム画面へ移動中... <a href="./index.html" style="color:#63b3ed;">移動しない場合はこちら</a></p>
</body>
</html>
"""
    with open(f"share{i}.html", "w", encoding="utf-8") as f:
        f.write(html)

print("✓ share0.html 〜 share10.html を再生成しました！")