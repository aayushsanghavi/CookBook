# -*- coding: utf-8 -*-

db.define_table('recipe',
               Field('title',requires=IS_NOT_EMPTY()),
               Field('image','upload',requires=IS_IMAGE(extensions=('jpeg','png','jpg','gif','bmp'))),
               Field('short_description',requires=IS_NOT_EMPTY()),
               Field('ingredients','text',requires=IS_NOT_EMPTY()),
               Field('how_to','text',requires=IS_NOT_EMPTY()),
               Field('votes','integer',default=0,readable=False,writable=False),
               auth.signature)

db.define_table('vote',
               Field('recipe','reference recipe'),
               Field('score','integer',default=+1),
               auth.signature)

db.define_table('comm',
               Field('recipe','reference recipe',readable=False,writable=False),
               Field('body','text'),
               Field('votes','integer',readable=False,writable=False,default=0),
               auth.signature)

db.define_table('comm_vote',
               Field('comm','reference comm'),
               Field('score','integer',default=+1),
               auth.signature)

def author(id):
    if id is None:
        return "Unknown"
    else:
        user = db.auth_user(id)
        return A('%(first_name)s %(last_name)s' % user, _href=URL('my_recipes',args=user.id))

def written_by(id):
    user = db.auth_user(id)
    return '%(first_name)s %(last_name)s' % user
