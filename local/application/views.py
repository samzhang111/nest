from flask import render_template
from application import application

@application.route("/")
def index():
    comments = [
            {   'id': 1,
                'author': 'schmidt',
                'body': 'merp',
                'parent-id':1,
               'depth': 1,
               'lineage': "1"
            },
            {   'id':2,
                'author': 'tom',
                'body': 'wait',
                'parent-id':1,
                'depth':2,
                'lineage': "1-2" 
                },
            {   'id':3,
                'author': 'john',
                'body': 'sup',
                'parent-id':3,
                'depth':1,
                'lineage': "3" 
                
                }
            ]
    return render_template("index.html", comments=comments)
