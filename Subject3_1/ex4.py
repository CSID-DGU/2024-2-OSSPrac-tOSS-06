from flask import Flask, render_template, request

app = Flask(__name__)

# 루트 경로 - 사용자 입력 폼을 표시
@app.route('/')
def input():
    return render_template('input.html')

# 결과 출력, 리스트로 데이터 받기
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method =='POST':
       result=dict()
       result['Gender']=request.form.get('gender')

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

