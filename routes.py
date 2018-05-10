from flask import render_template,redirect,flash
from app import sam
from app.forms import LoginForm

@sam.route('/')
@sam.route('/index')
def index():
    user = {'username': 'Sameer'}
    posts = [
        {
            'author': {'username': 'Sameer'},
            'body': 'First day in Office'
        },
        {
            'author': {'username': 'Basha'},
            'body': 'Chandigarh is a Clean City'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@sam.route('/login',methods=['GET','POST'] )
def login():
    	form=LoginForm()
    	if form.validate_on_submit():
    		flash('Login Requested for user {}, remembe_me={}'.format(form.username.data,form.remember_me.data))
    		return redirect (url_for('index'))
    	return render_template('login.html',title='signin',form=form)    