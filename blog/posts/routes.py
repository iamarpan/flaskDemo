from flask import Blueprint,flash,redirect,url_for,render_template,abort

from flask_login import login_required,current_user
from blog.models import Post
from blog.posts.forms import PostsForm
from blog import db

posts = Blueprint('posts',__name__)


@posts.route("/post/new",methods=["GET","POST"])
@login_required
def create_posts():
    form = PostsForm()
    if form.validate_on_submit():
        flash("Your post has been submitted")
        post = Post(title=form.title.data,content=form.title.data,user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template("create_post.html",title="Post",form=form,legend="New Post")


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html",title="Post",post=post)


@posts.route("/post/<int:post_id>/update",methods=["GET","POST"])
@login_required
def update_post(post_id):
    post = PostsForm()
    data = Post.query.get_or_404(post_id)
    if(current_user.id!=data.user_id):
        abort(403)
    if post.validate_on_submit():
        data.title = post.title.data
        data.content = post.content.data
        db.session.commit()
        return redirect(url_for('main.home'))
    post.title.data = data.title
    post.content.data = data.content
    return render_template("create_post.html",title="Update Post",form=post,legend="Update Post")


@posts.route('/post/<int:post_id>/delete',methods=["GET","POST"])
@login_required
def delete_post(post_id):

    post = Post.query.get_or_404(post_id)
    if(current_user.id != post.user_id):
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash("Post deleted Successfully")
    return redirect(url_for('main.home'))