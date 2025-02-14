from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)

    #수정
    # 수정 확인ㄴㅇㅎㅋㄴㅇㅎㅋㄴㅇㅀㅋㄴㅇㄿㄴ
#재재재재재수정