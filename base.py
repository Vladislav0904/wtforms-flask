from flask import Flask, url_for, request, render_template, redirect

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        return render_template('training.html', ing=True)
    else:
        return render_template('training.html')


@app.route('/list_prof/<list>')
def list_prof(list):
    specialities = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
                    'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                    'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман',
                    'пилот дронов']
    if 'ol' in list or 'ul' in list:
        return render_template('prof_list.html', list=list, specialities=specialities)
    else:
        return 'Передан неверный параметр. Используйте "ol" или "ul"!'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
