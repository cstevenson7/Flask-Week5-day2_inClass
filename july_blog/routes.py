from july_blog import app
from flask import render_template, request
#Import the form
from july_blog.forms import UserInfoForm
from july_blog.forms import BlogPostForm


#Home page route
@app.route('/')  # decorator
def home():
    customer_name= "Cindy"
    order_number = 1
    item_dict= {1:"Ice Cream", 2: "Bread", 3:"lemons", 4:"cereal"}
    return render_template("home.html", customer_name = customer_name, order_number = order_number, item_dict = item_dict)

#Register route
@app.route('/register', methods= ['GET','POST'])  # decorator
def register():
    form = UserInfoForm()
    #form.validate is checking the CSFR token thing, if the request is a GET it just renders the form
    # if the request == post then the user in fo entered is SENT
    if request.method == 'POST' and form.validate():
        #Get Information
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print("\n", username,password,email)  # this will print out in terminal


    return render_template("register.html", form=form)

#Create a blog route
@app.route('/creatposts', methods=['GET', 'POST'])
def createposts():
    form = BlogPostForm()
    if request.method == 'POST' and form.validate():
        title= form.title.data
        content = form.content.data 
        print("\n",title, content)   ## this will print out in terminal
    return render_template("createposts.html", form=form)