from flask import Flask, render_template

# 현재 모듈(파일)의 이름을 가져와 애플리케이션의 루트 경로를 알수있도록 한다
app = Flask(__name__)

# 차트 데이터. 각각 일,온도,습도
chart_Data = [
        [1,  37.8, 80.8],
        [2,  30.9, 69.5],
        [3,  25.4,   57],
        [4,  11.7, 18.8],
        [5,  11.9, 17.6],
        [6,   8.8, 13.6],
        [7,   7.6, 12.3],
        [8,  12.3, 29.2],
        [9,  16.9, 42.9],
        [10, 12.8, 30.9],
        [11,  5.3,  7.9],
        [12,  6.6,  8.4],
        [13,  4.8,  6.3],
        [14,  4.2,  6.2]]

@app.route('/') # 경로 지정
def hello():
    #return "hello22222" # hello 문자열 반환
    return render_template("index.html") 

# templates 폴더 내부에 있는 index.html 반환
#@app.route('/home')
#def example():
    #hello = "안녕하세요?"
    # 이때, 두번째 인자부터 값을 전달한다.
    # html에 표시할 변수이름=값
    #return render_template("index.html", user_name=hello) 

@app.route('/grap')
def grap():
    return render_template("grap.html", chartData=chart_Data)

@app.route('/camera')
def camera():
    return render_template("camera.html")

def main():
    # ip주소, debug, port 번호 실행
    app.run(host='127.0.0.1', debug=True, port=443)

if __name__ == '__main__':
    main()