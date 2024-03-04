from flask import Flask, request, jsonify
from personal_color_analysis import personal_color
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# uploads 디렉토리가 없으면 생성하는 함수
def create_upload_folder():
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/analyze', methods=['POST'])
def analyze_image():
    create_upload_folder()  # 디렉토리 생성

    if 'file' not in request.files:
        return jsonify({'error': '파일이 없습니다'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': '선택된 파일이 없습니다'})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        result = personal_color.analysis(filepath)

        return jsonify({'result': result})
    else:
        return jsonify({'error': '유효하지 않은 파일 형식입니다'})

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)