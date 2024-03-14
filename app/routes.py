from flask import abort, render_template, url_for, redirect, request, flash, session
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from app import app, db
from app.models import User, Post
from app.forms import LoginForm, RegisterForm, PostForm, UpdateUserForm
from sqlalchemy import exc
from werkzeug.security import check_password_hash, generate_password_hash
from http import HTTPStatus
from app.functions import get_posts, get_post


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

"""
    Rotas para User
"""
@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()

    user_name = form.user_name.data
    password = form.password.data
    cat_name = form.cat_name.data
    cat_sex = form.cat_sex.data

    if form.validate_on_submit():
        error = None

        user = User(user_name=user_name, password=generate_password_hash(password), cat_name=cat_name, cat_sex=cat_sex)

        try:
            db.session.add(user)
            db.session.commit()
        except exc.IntegrityError:
            error = f'User {user_name} is already registered.'

        else:
            return redirect(url_for('login'))


        flash(error)
    return render_template('/auth/register.html', form=form)


@app.route('/login', methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()

    form_user_name = form.user_name.data
    form_password = form.password.data 

    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form_user_name).first()
        error = None

        if user is None or not check_password_hash(user.password, form_password):
            error = "This user wasn't registered or password is incorrect"     
            flash(error)
            return redirect(url_for('login'))
        
        login_user(user)
        session.permanent = True
        return render_template('/blog/blog.html', posts=get_posts())

    return render_template('/auth/login.html', form=form)


@app.route('/user_update/<int:user_id>', methods=('GET', 'POST'))
@login_required
def user_update(user_id):

    form = UpdateUserForm()

    user = User.query.get(user_id)

    buffer_name = current_user.user_name

    user.user_name = form.user_name.data
    user.cat_name = form.cat_name.data
    user.cat_sex = form.cat_sex.data


    if request.method == 'POST':
        db.session.commit()
        flash(f'{user.user_name} has been updated')

    return render_template('/auth/update.html', form=form, user_name=buffer_name)


@app.route('/user_delete/<int:user_id>', methods=('GET', 'POST'))
def user_delete(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f'The the user was deleted.')
    return redirect(url_for('blog'))



"""
    Rotas para posts
"""
@app.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    form = PostForm()

    form_title = form.title.data
    form_body = form.body.data
    path_image='caminho/teste'

    if request.method == 'POST':
        post = Post(title=form_title, body=form_body, path_image=path_image, author_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        posts = get_posts()   
        return redirect(url_for('blog', posts=posts))

    return render_template('/blog/create.html', form=form)


@app.route('/post_update/<int:post_id>', methods=('GET', 'POST'))
@login_required
def post_update(post_id):

    form = PostForm()

    post = Post.query.get(post_id)

    buffer_post_name = post.title

    post.title = form.title.data
    post.body = form.body.data
    post.path_image = 'caminho'

    if request.method == 'POST':
        db.session.commit()
        flash(f'{post.title} has been updated')

    return render_template('/blog/update.html', form=form, post_name=buffer_post_name, post_id=post_id)


@app.route('/post_delete/<int:post_id>', methods=('GET', 'POST'))
def post_delete(post_id):
    db.session.query(Post).filter(Post.id==post_id).delete(synchronize_session='fetch')
    db.session.commit()
    flash(f'The post was deleted.')
    return redirect(url_for('blog'))


"""
    Rotas gerais
"""
@app.route('/blog')
def blog():
    return render_template('/blog/blog.html', posts=get_posts())


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('blog'))


@app.route('/')
def index():
    return render_template('/blog/blog.html', posts=get_posts())


@app.route('/self')
@login_required
def self():
    return render_template('/perfil/self.html')


@login_manager.unauthorized_handler
def unauthorized():
    if request.blueprint == 'api':
        abort(HTTPStatus.UNAUTHORIZED)
    return redirect(url_for('blog'))