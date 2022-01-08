import random
import string
import glob, os
from flask import request
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = '-mYrZF_M:uF-N#&Bi6M"dV4Og_Q8sO3IZE>Bdv(q<o!}t!3pU9#z%ugwzgCI_6'

a, b, c, d, e, f, g = random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0,
                                                                                    9), random.randint( 0, 9), random.randint(0, 9), random.randint(0, 9),

bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
    url = StringField('Enter a URL to be shortened : ', validators=[DataRequired()])
    submit = SubmitField('Submit')


def create_link(page):
    global linkparam
    linkparam = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
    #linkparam = str(hashlib.sha224(page.encode('utf8')).hexdigest())[0:7]
    print(linkparam)
    print(f"Creating link on https://l-nqs.herokuapp.com/{linkparam}")
    f = open(f'C:/Users/xpyth/OneDrive/Documents/GitHub/l-nqs/templates/{linkparam}.html', 'x')
    with open(f'C:/Users/xpyth/OneDrive/Documents/GitHub/l-nqs/templates/{linkparam}.html', 'w+') as linkhtml :
        markup = f'''
<!DOCTYPE html>
<html>
    <head>
        <title>Redirecting...</title>
    </head>
    <body>
        <script>
            window.location.replace("{page}");
            var path = window.location.pathname;
            var page = path.split("/").pop();
        </script>    
    </body>
</html>
'''
        linkhtml.write(markup)

        f = open(f'C:/Users/xpyth/OneDrive/Documents/GitHub/l-nqs/templates/{linkparam}2.html', 'x')
        with open(f'C:/Users/xpyth/OneDrive/Documents/GitHub/l-nqs/templates/{linkparam}2.html', 'w+') as linkhtmld:
            linkhtmld.write(f'<h3>https://l-nqs.herokuapp.com/{linkparam}</h3>')
        os.chdir("C:/Users/xpyth/OneDrive/Documents/GitHub/l-nqs/templates")
        file = glob.glob("*.html")
        functionName = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(8))
        exec(f'''
@app.route(f'/{linkparam}')
def {functionName}():
    return render_template(f'{linkparam}.html')
        ''')


os.chdir("C:/Users/xpyth/OneDrive/Documents/GitHub/l-nqs/templates")
file = glob.glob("*.html")
fileWithoutExtention = [item.replace(".html", "") for item in file]
print(file)
print(fileWithoutExtention)
for i in range(len(file) - 1) :
    print(f'/{fileWithoutExtention[i]}')
    functionName = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(8))
    exec(f'''
@app.route(f'/{fileWithoutExtention[i]}')
def {functionName}():
    return render_template(f'{file[i]}')
    ''')

@app.route('/')
def default_route():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.route('/create', methods=['GET', 'POST'])
def create():
    form_data = request.form
    data = str(form_data)
    data = data.replace("ImmutableMultiDict([('url', '", "")
    data = data.replace("')])", "")
    print(data)
    create_link(data)
    tmpdata = ""
    try:
        print(request.form)
        return render_template('about.html', data=tmpdata)
    finally:
        print(request.form['submit_button'])
        '''
        if request.form['submit_button'] == 'submitted':
            dir = "C:/Users/xpyth/OneDrive/Documents/Github/l-nqs/templates"
            directory = os.listdir(dir)

            searchstring = data

            for fname in directory:
                if os.path.isfile(dir + os.sep + fname):
                    # Full path
                    f = open(dir + os.sep + fname, 'r')

                    if searchstring in f.read():
                        print('found string in file %s' % fname)
                    else:
                        print('string not found')
                    f.close()
        
        '''
        create_link(data)
        tmpdata = linkparam

@app.route('/join')
def join():
    return render_template('join.html')

if __name__ == '__main__':
    app.run()


