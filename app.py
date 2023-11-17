# app.py

from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# API데이터 출처
# http://data.seoul.go.kr/dataList/OA-15486/S/1/datasetView.do 
# 서울시 문화행사 정보 API 엔드포인트
API_URL = "http://openapi.seoul.go.kr:8088/"
API_ENDPOINT = "/json/culturalEventInfo/1/100"
API_KEY = "7946634a496c616e3836574f675945"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events')
def get_events():
    
    #요청 파라미터 받기
    guName = request.form.get('data')

    # API를 통해 문화행사 정보 가져오기
    response = requests.get(f"{API_URL}{API_KEY}{API_ENDPOINT}")
    data = response.json()

    # 필요한 데이터 추출
    events = data['culturalEventInfo']['row']

    districts = []
    for event in events:
        # 프런트에서 선택한 자치구와 일치하는지 확인
        if(event['GUNAME'] == request.args.get('data')):
            print('sucess if')
            # 뷰로 전달할 데이터
            district = {'CODENAME': event['CODENAME'], 'TITLE': event['TITLE'], 'DATE' : event['DATE'], 'GUNAME' : event['GUNAME'], 'PLACE' : event['PLACE'], 'location' : [event['LOT'], event['LAT']], 'MAIN_IMG' : event['MAIN_IMG']  }
            
            # 데이터를 잘 파싱하였는지 로그 출력
            print(event)

            districts.append(district)  

    return render_template('index.html', events = districts )

@app.route('/eventsScript')
def get_eventsScript():

    # API를 통해 문화행사 정보 가져오기
    response = requests.get(f"{API_URL}{API_KEY}{API_ENDPOINT}")
    data = response.json()

    # 필요한 데이터 추출
    events = data['culturalEventInfo']['row']

    districts = []
    for event in events:
        # 뷰로 전달할 데이터
        district = {'CODENAME': event['CODENAME'], 'TITLE': event['TITLE'], 'DATE' : event['DATE'], 'GUNAME' : event['GUNAME'], 'PLACE' : event['PLACE'], 'location' : [event['LOT'], event['LAT']]}
         
        # 데이터를 잘 파싱하였는지 로그 출력
        print(event)

        districts.append(district) 

    return districts
    
if __name__ == '__main__':
    app.run(debug=True)
