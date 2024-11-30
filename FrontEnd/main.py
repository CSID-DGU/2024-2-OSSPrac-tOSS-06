from flask import Flask, render_template, request
import requests  # BackEnd와 통신하기 위해 사용
import logging # 로그 메시지 확인용

app = Flask(__name__)

# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html')

# 학생 정보 입력 페이지
@app.route('/input')
def input():
    return render_template('input.html')

# 결과 페이지 (BackEnd 호출 추가)
@app.route('/result', methods=['POST'])
def result():
    # 사용자로부터 입력 받은 데이터
    names = request.form.getlist('name[]')
    roles = request.form.getlist('role[]')
    majors = request.form.getlist('major[]')
    phone_numbers = request.form.getlist('PhoneNumber[]')
    emails = request.form.getlist('email[]')
    
    # BackEnd에 전달할 데이터 생성
    payload = {
        "names": names,
        "roles": roles,
        "majors": majors,
        "phone_numbers": phone_numbers,
        "emails": emails
    }
    
    # BackEnd API 호출
    try:
        response = requests.post("http://backapp:8000/process_students", json=payload)
        students = response.json()  # BackEnd에서 받은 데이터
    except Exception as e:
        print("Error communicating with BackEnd:", e)
        students = []  # 에러 발생 시 빈 리스트 반환
    
    # 결과 페이지 렌더링
    return render_template('result.html', students=students)

# 연락처 페이지
@app.route('/contact')
def contact_info():
    return render_template('contact.html')

logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
