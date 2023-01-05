"""
Routes and views for the flask application.
"""
from itertools import product
from flask import request, url_for 
from datetime import datetime
from flask import render_template, redirect
from ProductAPIFlaskClient_1147129 import app
from Category import Category
from Product import Product 
from ServiceClient import ServiceClient

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/showproducts',methods=['GET','POST'])
def showproducts(): 
    sc = ServiceClient() 
    products = sc.get_all_products() 
    cats = sc.get_categories() 
    catsel = 0 
    if len(request.form) > 0: 
        catsel =  request.form['catddl'] # posted data dropdon value 
        #print("sssss: ")
        #print(catsel)
        products = sc.get_products_by_category(catsel)
        #json.loads(d)['onsale'],
        #json.loads(d)['Discontinued'])
    return render_template( 
        'showproducts.html', 
        title='Show Products', 
        prods=products, 
        catlist = cats, 
        catselected = int(catsel), 
        message='Your application description page.' 
    ) 
 
@app.route('/addnewproduct',methods=['GET','POST']) 
def addnewproduct(): 
    sc = ServiceClient()
    catsel = 100 
    res = '' 
    #print("outside")
    #print(request.form)
    if len(request.form) > 0: 
        #print("post")
        if request.method == "POST":
            # print(request.form['Discontinued'])
            #print("post req")
            prod = Product() 
            prod.product_id = int(request.form['product_id'])
            prod.product_name = request.form['product_name'] 
            prod.description = request.form['description'] 
            prod.price = float(request.form['price'])
            prod.stock_level = request.form['stock_level'] 
            prod.category_id =  int(request.form['category_id']) # posted data 
            prod.onsale =  bool(request.form['onsale'])
            prod.Discontinued =  False #bool(request.form['Discontinued'])
            res = sc.add_new_product(prod) 
        #msg = res 
    cats = sc.get_categories() 
    return render_template( 
        'addnewproduct.html', 
        title='Add New Product', 
        catlist = cats, 
        msg=res
        )

@app.route('/updateproduct/<int:product_id>',methods=['GET','POST']) 
def updateproduct(product_id): 
    sc = ServiceClient()
    print("before")
    print(product_id)
    print("after")
    prod = sc.get_products_by_pid(product_id)
    catsel = 100 
    res = '' 
    print("outside")
    if len(request.form) > 0: 
        print("put")
        if request.method == "POST":
            # print(request.form['Discontinued'])
            print("post req")
            if(request.form.get('onsale',type=bool)==None):
                print(False)
            else:
                print(request.form.get('onsale',type=bool))
            print("sss")
            check = lambda a:True if a==True else False
            print(check(request.form.get('onsale',type=bool)))
            prod.product_id = int(request.form['product_id'])
            prod.product_name = request.form['product_name'] 
            prod.description = request.form['description'] 
            prod.price = float(request.form['price'])
            prod.stock_level = request.form['stock_level'] 
            prod.category_id =  int(request.form['category_id']) # posted data 
            prod.onsale =  check(request.form.get('onsale',type=bool))
            prod.Discontinued =  check(request.form.get('Discontinued',type=bool))
            res = sc.update_product(prod) 
        #msg = res 
            print(res)
    cats = sc.get_categories() 
    return render_template( 
        'updateproduct.html',
        title='Update Product', 
        catlist = cats, 
        msg=res,
        prod=prod
        )
@app.route('/deleteproduct/<int:product_id>',methods=['GET']) 
def deleteproduct(product_id): 
    print("ssccc")
    sc = ServiceClient()
    print(product_id)
    if product_id:
        print("dhukse")
        res = sc.delete_product(product_id)
    return redirect(url_for('showproducts'))