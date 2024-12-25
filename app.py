from flask import Flask, send_from_directory

app = Flask(__name__)

# 设置 HTML 文件所在的目录
HTML_DIR = "./"

@app.route("/")
def serve_gym_html():
    # 返回 gym.html 文件
    return send_from_directory(HTML_DIR, "./templates/index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8890)
