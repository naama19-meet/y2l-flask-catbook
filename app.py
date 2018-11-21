from flask import Flask
from flask import *
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def cat_profile(id):
	cat = get_cat_id(id)
	return render_template("cat.html", cat = cat)


@app.route('/new',methods=['GET','POST'])
def create_cat():
	if request.method == 'GET':
		return render_template("newcat.html")
	else:
		name = request.form['newcatname']
		cat_object = Cat(name=name)
		session.add(cat_object)
		session.commit()
		return redirect(url_for('catbook_home'))


if __name__ == '__main__':
   app.run(debug = True)
