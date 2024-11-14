# aduinoCapstoneProject
아두이노 보드를 활용한 실시간 식물 케어 웹서비스

<br/><br/>

## yolov5 학습 코드 및 데이터셋
[<img src="https://img.shields.io/badge/Colab-F7DF1E.svg?style=for-the-badge&logo=googlecolab&logoColor=#F9AB00"/>](https://github.com/HwangWooJin1028/aduinoCapstoneProject/blob/main/%EC%83%81%EC%B6%94_%ED%83%90%EC%A7%80_%EB%AA%A8%EB%8D%B8_train_%EB%8D%B0%EC%9D%B4%ED%84%B0_%EC%A1%B0%EC%A0%95.ipynb)
[<img src="https://img.shields.io/badge/roboflow-5C2D91?style=for-the-badge&logo=roboflow&logoColor=white">](https://universe.roboflow.com/project-0rxid/aquaponic_polygan_test)

- google colab에 사본 저장 뒤 코드 차례로 실행하여 모델 학습
- lettuce_result 에 저장된 best.pt 파일 다운로드
- 다운로드된 best.pt를 이용하여 esp32cam_detect.py 코드를 이용하여 <br/> 스트리밍 되고 있는 영상을 객체탐지하여 box 표시 후 순차적으로 클라이언트에 전송
  - ai_test_nativeapp.py 는 네이티브 프로그램 코드.
  - esp32cam_detect.py는 template 내부에 있는 camera.html에 존재하는 <br/>
    <img src="{{ url_for('video_feed') }}"...> (camera.html의 186번째) 에 의해 호출
- 자세한 내용은 코드 내 주석 확인

- 아래는 본 프로젝트에서 사용하는 모델의 학습 결과<br/>

![image](https://github.com/user-attachments/assets/a14df1bb-0aaa-4f83-a008-5d476e4ab70e)

<br/><br/>


## node.js 이용하여 chatapi 사용하기
1. node.js를 설치한다.<br/>
2. terminer에 node .\index.js를 넣어 출력을한다.<br/>
3. npm init를 터미널 창에 넣는다.<br/>
3. npm install openai<br/>
4. usage에 있는 것을 복사 한다.<br/>
5. openai키에 api키를 발급하여 넣는다.<br/>

