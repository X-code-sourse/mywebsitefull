import os
from flask import Flask, render_template, request

app = Flask(__name__)

# 简单留言列表（程序运行期间有效）
messages = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        msg = request.form.get("message")
        if msg:
            messages.append(msg)
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    # 获取 Render 提供的端口，默认 5000
    port = int(os.environ.get("PORT", 5000))
    # 监听所有 IP 地址
    app.run(host="0.0.0.0", port=port)
