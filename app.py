from flask import Flask, render_template, request

app = Flask(__name__)

# 存储留言的简单列表（程序运行期间有效）
messages = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        msg = request.form.get("message")
        if msg:
            messages.append(msg)
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)