"""
Simple file manager with flask
source: https://www.youtube.com/watch?v=c9QY27ISqI0
"""
import os
import subprocess
from flask import Flask, render_template_string, redirect, request, send_file

app = Flask(__name__)


@app.route('/')
def root():
    return render_template_string("""
    <html>
        <head>
            <title>File Manager</title>
        </head>
        <body>
            <div align="center">
                <h1 >Local file system</h1>
                <p>CWD: <strong>{{ current_working_directory }}</strong></p>
            </div>
            <ul>
                <li><a href="/cd?path=..">..</a></li>
                {% for item in file_list[0:-1] %}
                    {% if '.' not in item %}
                        <li><strong><a href="/cd?path={{ current_working_directory + "/" + item }}">{{item}}</a></strong> <span style="margin-left: 3rem"><a href="/rm?item={{item}}">DELETE</a></span> <span style="margin-left: 3rem"><a href="/download?item={{item}}">Download</a></span></li>
                    {% elif '.txt' or '.py' or '.csv' in item%} 
                        <li><strong><a href="/view?file={{ current_working_directory + "/" + item }}">{{item}}</a></strong> <span style="margin-left: 3rem"><a href="/rm?item={{item}}">DELETE</a></span> <span style="margin-left: 3rem"><a href="/download?item={{item}}">Download</a></span> </li>
                        
                    {% else %}
                        <li>{{item}} <span style="margin-left: 3rem"><a href="/rm?item={{item}}">DELETE</a></span> <span style="margin-left: 3rem"><a href="/download?item={{item}}">Download</a></span> </li> 
                    {% endif%}
                {% endfor %}
            </ul>
        </body>
    </html>
    """, current_working_directory=os.getcwd(),
                                  file_list=subprocess.check_output('ls', shell=True).decode('UTF-8').split('\n'))


@app.route('/cd')
def cd():
    # run 'levelup' command
    os.chdir(request.args.get('path'))

    # redicert to file manager
    return redirect('/')


@app.route('/rm')
def rm():
    os.remove(request.args.get('item'))

    return redirect('/')

# file downloader


@app.route('/download')
def downloadFile():
    # For windows you need to use drive name [ex: F:/Example.pdf]
    return send_file(request.args.get('item'), as_attachment=True)


@app.route('/view')
def view():
    return subprocess.check_output('cat ' + request.args.get('file'), shell=True).decode('UTF-8').replace('\n', '<br>')


if __name__ == "__main__":
    app.run(debug=True)
