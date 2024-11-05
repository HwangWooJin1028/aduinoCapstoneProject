# 로고 이미지 301*52 사이즈로 바꾸기
from flask import Flask, request, render_template
import os
import sensor_utils
import database_connect
import ThingSpeak_connect
import ex


# 현재 모듈(파일)의 이름을 가져와 애플리케이션의 루트 경로를 알수있도록 한다
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'  # Directory where uploaded files will be saved
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

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
    # 임의로 /grap에 들어갈때 db에 저장하는 걸로 코드를 정함. 나중에 이건 바꾸기

    # 1. 온도 평균하고 습도 평균을 구하고 저장한다.
    # temp_avg, humi_avg = sensor_utils.calculate_averages(sensor_utils.load_sensor_data())
    
    # 2. db에 connect하는 py 파일을 통해 db에 연결
    # database_connect.save_sensordata_db(temp_avg, humi_avg)

    # 웹 그래프에 나타낼 최근 10개의 데이터를 가져오기
    temp_chart_Data = ThingSpeak_connect.get_sensor_data()
    
    # 웹에 나타낼 최근 1개의 데이터를 가져오기
    temp,humi = ThingSpeak_connect.get_sensor_data_one()
    
    # 최근 1개 데이터를 txt 파일에 저장
    sensor_utils.save_sensor_data(temp, humi)

    return render_template("grap.html", chartData=temp_chart_Data, oneTempData=temp, oneHumiData=humi)

@app.route('/camera')
def camera():
    return render_template("camera.html")

# ESP32 cam 영상 보여주기 예제
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    return render_template('image_show.html')

def main():
    # ip주소, debug, port 번호 실행
    app.run(host='0.0.0.0', debug=True, port=443)

if __name__ == '__main__':
    main()