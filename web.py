from flask import Flask, render_template

app = Flask(__name__)


# 创建了网址 、show/info/和函数index的对应关系
# 以后用户在浏览器上访问 /show/info,网站自动执行index
@app.route("/show/info")
def index():
    return render_template("super_link.html")


@app.route("/get/news")
def get_news():
    return render_template("news.html")


if __name__ == "__main__":
    app.run()
