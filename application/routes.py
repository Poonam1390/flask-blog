from application.models import Posts
from flask import render_template, redirect, url_for
from application import app, db
from application.forms import PostForm

@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        postData = Posts(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            title = form.title.data,
            content = form.content.data
        )

        db.session.add(postData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('post.html', title='Post', form=form)


@app.route('/')
@app.route('/home')
def home():
    postData = Posts.query.all()
    #postfirstname = Posts.query.get(first_name)
    #postlastname = Posts.query.get(last_name)
    #postcontent = Posts.query.get(content)
    return render_template('home.html', title='HomePage',posts=postData)


@app.route('/about')
def about():
    return render_template('about.html', title='This is the about page', body='This is the body but we are mising the head')



@app.route('/register')
def register():
    return render_template('register.html',title='Register',body='Please register yourself on here',head='Register here!!!')