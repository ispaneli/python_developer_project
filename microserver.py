from flask import Flask, request, send_file
import os
from main import clone_voice

app = Flask(__name__)

# Директория для сохранения файлов
uploads_dir = os.path.join(app.instance_path, 'uploads')


@app.route('/', methods=['GET', 'POST'])
def clone_server():
    """
        Функция для внешнего обращения к нашей модели. На вход
        поступает текст и экземпляр голоса, берем их из запроса.
        Сохраняем переданные голоса, для дальнейшего обучения нашей
        модели.

        :return: возвращаем результат модели клиенту
    """
    if request.method == 'GET':
        return 'Server ready to work!'

    if request.method == 'POST':
        text = request.form['text']
        file = request.files['audio']
        clone_path = os.path.join(uploads_dir, file.filename)
        file.save(clone_path)
        clone_voice(clone_path, text, 'result.wav', play_result=True)
        return send_file('result.wav', mimetype='audio/vnd.wave')


if __name__ == "__main__":
    app.run(host='192.168.1.98', port=5005)
