# coding: utf8
# intente algo como
def index():
    return {'a':10,'b':'hola'}

# edito la vista demo/indexpimp.html
def indexpimp():
    session.b = session.get('b',0) + 1
    mensaje = 'la variable %s' % session.b
    return locals()
    #return {'mensaje':'my sting'}

def navegador():
    x= request.env.http_accept_language
    return "datos del cliente: %s" %x

def argumentos():
    # ...argumentos/1/2/3 | return json
    # x = request.args
    # ...argumentos/?a=hola | return json
    import cgi
    y = request.vars
    return "datos del cliente: %s __" % cgi.escape(str(y))

def redirectin():
    redirect(URL('redirectout', args=['primer', 'segundo_argumento'], vars={'hola':'argumentos_con_vars', 'otro': 'campo week'}))

def redirectout():
    x = request.args
    y = request.vars
    return 'hola, esto son los datos entrantes __ args: %s  || vars: %s' % (x,SPAN(y))

# Formularios
def miform():
    form = SQLFORM.factory(Field('equipo', requires=IS_NOT_EMPTY()),
                           Field('edad', 'date')).process()
    if form.accepted:
       session.flash = 'buena'
       redirect(URL('rform', vars={'equipo':form.vars.equipo, 'edad':form.vars.edad}))
    elif form.errors:
       response.flash = 'algo paso'
    else:
       response.flash = 'el formulario!'
    return locals()

def rform():
    x = 'SI gane: %s ! %s' % (request.vars.equipo, request.vars.edad)
    return locals()

def formdata():
    form = SQLFORM(db.blog_post).process()
    rows = db(db.blog_post).select()
    return locals()

def show():
    post = db.blog_post(request.args(0, cast=int))
    return locals()
