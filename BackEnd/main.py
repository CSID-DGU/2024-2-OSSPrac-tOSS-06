from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/picture'

@app.route('/process_students', methods=['POST'])
def process_students():
    data = request.json
    names = data.get('names', [])
    roles = data.get('roles', [])
    majors = data.get('majors', [])
    phone_numbers = data.get('phone_numbers', [])
    emails = data.get('emails', [])

    students = []
    for i in range(len(names)):
        # 한글 이름을 그대로 파일 이름으로 사용
        picture_filename = f"{names[i].strip()}.png"
        picture_path = os.path.join(app.config['UPLOAD_FOLDER'], picture_filename)

        # 로그로 현재 파일 경로 확인
        app.logger.debug(f"Looking for file: {picture_path}")

        # 파일이 없으면 기본 이미지 사용
        if not os.path.isfile(picture_path):
            app.logger.debug(f"File not found: {picture_path}, using default.png")
            picture_filename = "default.png"

        students.append({
            "name": names[i],
            "role": roles[i],
            "major": majors[i],
            "phone_number": phone_numbers[i],
            "email": emails[i],
            "picture": picture_filename
        })

    return jsonify(students)

# 정적 파일 제공 엔드포인트
@app.route('/static/picture/<path:filename>')
def serve_picture(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except Exception as e:
        app.logger.error(f"Error serving file {filename}: {e}")
        return "File not found", 404

if __name__ == '__main__':
    # Docker 환경에서 외부 접근을 위해 host='0.0.0.0' 설정
    app.run(host='0.0.0.0', port=8000, debug=True)