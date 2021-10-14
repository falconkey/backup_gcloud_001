import datetime
import os
from flask import Flask, render_template, send_from_directory, request, Response
#import xx # this will be your file name; minus the `.py`



app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home_index.html')

@app.route('/tt')
def tt_home_page():
    return render_template('tt_index.html')

@app.route('/tt_dic_index')
def tt_dic_page():
    return render_template('tt_dic_index.html')

@app.route('/tt_cic_index')
def tt_cic_page():
    return render_template('tt_cic_index.html')

@app.route('/pdf_files/tt/ccbt21001.pdf') #the url you'll send the user to when he wants the pdf
def ccbt21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'ccbt21001.pdf')

@app.route('/pdf_files/tt/ccec21001.pdf') #the url you'll send the user to when he wants the pdf
def ccec21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'ccec21001.pdf')

@app.route('/pdf_files/tt/ccjn21001.pdf') #the url you'll send the user to when he wants the pdf
def pdfviewer():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'ccjn21001.pdf')

@app.route('/pdf_files/tt/ccpd21001.pdf') #the url you'll send the user to when he wants the pdf
def ccpd21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'ccpd21001.pdf')

@app.route('/pdf_files/tt/ccpm21001.pdf') #the url you'll send the user to when he wants the pdf
def ccpm21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'ccpm21001.pdf')

@app.route('/pdf_files/tt/ccpp21001.pdf') #the url you'll send the user to when he wants the pdf
def ccpp21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'ccpp21001.pdf')

@app.route('/pdf_files/tt/ccss21001.pdf') #the url you'll send the user to when he wants the pdf
def ccss21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'ccss21001.pdf')

@app.route('/pdf_files/tt/dcba21001.pdf') #the url you'll send the user to when he wants the pdf
def dcba21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcba21001.pdf')

@app.route('/pdf_files/tt/dcbp21001.pdf') #the url you'll send the user to when he wants the pdf
def dcbp21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcbp21001.pdf')

@app.route('/pdf_files/tt/dcbp21002.pdf') #the url you'll send the user to when he wants the pdf
def dcbp21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcbp21002.pdf')

@app.route('/pdf_files/tt/dcec21001.pdf') #the url you'll send the user to when he wants the pdf
def dcec21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcec21001.pdf')

@app.route('/pdf_files/tt/dcec21002.pdf') #the url you'll send the user to when he wants the pdf
def dcec21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcec21002.pdf')

@app.route('/pdf_files/tt/dcjn21001.pdf') #the url you'll send the user to when he wants the pdf
def dcjn21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcjn21001.pdf')

@app.route('/pdf_files/tt/dcjn21002.pdf') #the url you'll send the user to when he wants the pdf
def dcjn21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcjn21002.pdf')

@app.route('/pdf_files/tt/dcpd21001.pdf') #the url you'll send the user to when he wants the pdf
def dcpd21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcpd21001.pdf')

@app.route('/pdf_files/tt/dcpd21002.pdf') #the url you'll send the user to when he wants the pdf
def dcpd21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcpd21002.pdf')

@app.route('/pdf_files/tt/dcpm21001.pdf') #the url you'll send the user to when he wants the pdf
def dcpm21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcpm21001.pdf')

@app.route('/pdf_files/tt/dcpp21001.pdf') #the url you'll send the user to when he wants the pdf
def dcpp21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcpp21001.pdf')

@app.route('/pdf_files/tt/dcpp21002.pdf') #the url you'll send the user to when he wants the pdf
def dcpp21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcpp21002.pdf')

@app.route('/pdf_files/tt/dcss21001.pdf') #the url you'll send the user to when he wants the pdf
def dcss21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcss21001.pdf')

@app.route('/pdf_files/tt/dcss21002.pdf') #the url you'll send the user to when he wants the pdf
def dcss21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcss21002.pdf')

@app.route('/upload_single_file', methods=['GET'])
def upload_single_file():
    return render_template('upload_single_file_home_index.html')

@app.route('/file/upload', methods=['POST'])
def upload_part():  # 接收前端上传的一个分片
    task = request.form.get('task_id')  # 获取文件的唯一标识符
    chunk = request.form.get('chunk', 0)  # 获取该分片在所有分片中的序号
    filename = '%s%s' % (task, chunk)  # 构造该分片的唯一标识符

    upload_file = request.files['file']
    upload_file.save('./upload/%s' % filename)  # 保存分片到本地
    return render_template('./index.html')


@app.route('/file/merge', methods=['GET'])
def upload_success():  # 按序读出分片内容，并写入新文件
    target_filename = request.args.get('filename')  # 获取上传文件的文件名
    task = request.args.get('task_id')  # 获取文件的唯一标识符
    chunk = 0  # 分片序号
    with open('./upload/%s' % target_filename, 'wb') as target_file:  # 创建新文件
        while True:
            try:
                filename = './upload/%s%d' % (task, chunk)
                source_file = open(filename, 'rb')  # 按序打开每个分片
                target_file.write(source_file.read())  # 读取分片内容写入新文件
                source_file.close()
            except IOError as msg: parser.error(str(msg));
            break

            chunk += 1
            os.remove(filename)  # 删除该分片，节约空间

    return render_template('./index.html')


@app.route('/file/list', methods=['GET'])
def file_list():
    files = os.listdir('./upload/')  # 获取文件目录
    files = map(lambda x: x if isinstance(x, unicode) else x.decode('utf-8'), files)  # 注意编码
    return render_template('./list.html', files=files)


@app.route('/file/download/<filename>', methods=['GET'])
def file_download(filename):
    def send_chunk():  # 流式读取
        store_path = './upload/%s' % filename
        with open(store_path, 'rb') as target_file:
            while True:
                chunk = target_file.read(20 * 1024 * 1024)
                if not chunk:
                    break
                yield chunk

    return Response(send_chunk(), content_type='application/octet-stream')




if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_render_template]
# [END gae_python38_render_template]
