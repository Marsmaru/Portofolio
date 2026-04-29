from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # List projects kamu
    projects = [
        {
            'title': 'Website HIMA PTI',
            'desc': 'Sistem informasi organisasi mahasiswa Pendidikan Teknologi Informasi.',
            'github': 'https://github.com/rasyidanur/hima-pti'
        },
        {
            'title': 'Game Edukasi Flash 8',
            'desc': 'Game interaktif menggunakan ActionScript 2.0 yang dibangun di Macromedia Flash 8.',
            'github': 'https://github.com/Marsmaru/flash8_coin_rush.git' # Link repo yang kamu buat tadi
        },
        {
            'title': 'Project Portofolio',
            'desc': 'Website portofolio pribadi menggunakan Python Flask dan CSS modern.',
            'github': '#'
        }
    ]
    return render_template('index.html', projects=projects)