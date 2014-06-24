# coding: utf8
# intente algo como
def index():
    rows = db(db.blog_post).select(orderby=db.blog_post.title.upper())
    return locals()

@auth.requires_login()
def create():
    # db.blog_post.time_stamp.default = request.now
    # db.blog_post.time_stamp.writable = False
    # db.blog_post.time_stamp.readable = False
    form = SQLFORM(db.blog_post).process()
    if form.accepted:
        session.flash = "nuevo post"
        redirect(URL('index'))
    return locals()

def show():
    row_post = db.blog_post(request.args(0, cast=int))
    db.blog_comment.blog_post.default = row_post.id
    db.blog_comment.blog_post.writable = False
    db.blog_comment.blog_post.readable = False
    form = SQLFORM(db.blog_comment).process()
    comments = db(db.blog_comment.blog_post==row_post.id).select()
    return locals()

@auth.requires_membership('managers')
def manager():
    grid = SQLFORM.grid(db.blog_post)
    return locals()
