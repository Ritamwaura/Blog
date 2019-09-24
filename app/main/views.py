
from . import main
from ..models import User,Post,Comment
from .. import db
from .forms import PostForm,CommentForm
from flask import render_template,redirect,url_for,abort
from flask_login import login_required,current_user
from ..email import mail_message
import datetime
import json 
import urllib.request,json
from ..request import getQuotes 
@main.route('/')
def index():
   blogs = Blog.query.all()
   '''
   View root page function that returns the index page and its q
   '''
   title = 'Home - Welcome to The best Blog Website Online'
   quote = getQuotes()
   quote1 = getQuotes()
   quote2 = getQuotes()
   quote3 = getQuotes()
   return render_template('index.html', title = title, blogs=blogs, quote=quote ,quote1=quote1,quote2=quote2,quote3=quote3 
@main.route('/')
#def indexblog():
    '''
    view root page function that returns index page & data
    '''
    posts = Post.query.order_by(Post.date_posted.desc()).limit(3).all()

    title = 'Home - Welcome to the M.M.A Blog'
    
    random=urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json').read()
    get_source_response = json.loads(random)
blog
This is a personal blogging website where you can create and share your opinions and other users can read and comment on them. This is an app that allows users to create and post their opinions on any topic of their interest. Other users can then read and comment on the opinions.

By Rita mwaura
BDD SPECIFICATIONS TABLE
User	User Action	Output
Writer	Create an Account	Fill the registration form and sign up
Write new blog posts	Click on Add a new Blog to add a new post
Delete a blog post	On the blog post, click on the delete post button
Delete comments from a post	On the comments, click the delete comment button
User	View Blog post on the site	Go to the home page to view the blog posts
Comment on a blog post	Click comment on any post
Subscribe to the blog	Fill in the subscription form and submit
Setup/Installation requirements
Ensure you have Python3.6 installed on your computer.
Clone this respository and navigate to where it has been saved.
Open the file in your editor and navigate to the start.sh file.
Enter your email address, email password and secret key.
Activate the virtual environment using this command: source virtual/bin/activate
Run chmod a+x on the terminal
Run ./start.sh on the terminal to open the app
Known Bugs
There are currently no known bugs in the application

Technologies Used
Python3.6
Flask
HTML
Bootstrap
Support and Contact Details
For more information, questions or help, feel free to reach me on email me at : emmanuel.muchiri@outlook.com


    return render_template('index.html',index=index, title=title, post=post, random=get_source_response)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_joined = user.date_joined.strftime('%b %d, %Y')

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,date = user_joined)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
   user = User.query.filter_by(username = uname).first()
   if user is None:
       abort(404)

   form = UpdateProfile()

   if form.validate_on_submit():
       user.bio = form.bio.data

       db.session.add(user)
       db.session.commit()

       return redirect(url_for('.profile',uname=user.username))

   return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
   user = User.query.filter_by(username = uname).first()

   if 'photo' in request.files:
       filename = photos.save(request.files['photo'])
       path = f'photos/{filename}'
       user.profile_pic_path = path
       db.session.commit()

   return redirect(url_for('main.profile',uname=uname))

@main.route('/post/new', methods = ['GET','POST'])
@login_required
def new_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        title = post_form.title.data
        text = post_form.text.data
        

        # Updated post instance
        new_post = Post(title=title,text=text)

        # Save post method
        new_post.save_post()
        return redirect(url_for('.index'))

    title = 'New post'
    return render_template('new_post.html',title = title,post_form=post_form )

@main.route('/posts')
def all_posts():
    posts = Post.query.order_by(Post.date_posted.desc()).all()

    title = 'Blog posts'

    return render_template('posts.html', title = title, posts = posts)

@main.route('/post/<int:id>',methods=['GET','POST'])
def post(id):

    form = CommentForm()
    post = Post.get_post(id)

    if form.validate_on_submit():
        comment = form.text.data

        new_comment = Comment(comment = comment,user = current_user,post = post.id)

        new_comment.save_comment()


    comments = Comment.get_comments(post)

    title = f'{post.title}'
    return render_template('post.html',title = title, post = post, form = form, comments = comments)

@main.route('/delete_comment/<id>/<post_id>',methods = ['GET','POST'])
def delete_comment(id,post_id):
    comment = Comment.query.filter_by(id = id).first()

    db.session.delete(comment)
    db.session.commit()

    return redirect(url_for('main.post',id = post_id))

@main.route('/delete_post/<id>',methods = ['GET','POST'])
def delete_post(id):
    post = Post.query.filter_by(id = id).first()

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('main.all_posts'))

@main.route('/subscribe/<id>')
def subscribe(id):
    user = User.query.filter_by(id = id).first()

    user.subscription = True

    db.session.commit()

    return redirect(url_for('main.index'))

@main.route('/post/update/<id>',methods = ['GET','POST'])
def update_post(id):
    form = PostForm()

    post = Post.query.filter_by(id = id).first()

    form.title.data = post.title
    form.text.data = post.text

    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data

        post.title = title
        post.text = text

        db.session.commit()

        return redirect(url_for('main.post',id = post.id))

    return render_template('update.html',form = form)

@main.route('/user/<uname>/blogs')
def user_blogs(uname):
    user = User.query.filter_by(username=uname).first()
    blogs = Post.query.filter_by(user_id = user.id).all()
    # blogs_count = Blog.count_blogs(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')

    return render_template("profile/blogs.html", user=user, posts=blogs,date = user_joined)