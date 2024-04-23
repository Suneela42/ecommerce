from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from flask import redirect
from booksapp.models import *
from booksapp.models import BookItem
from django.contrib.auth import authenticate
from django.contrib import messages
import mysql.connector as sql
#Register
name=""
email=""
blog=""
contact=""
country=""
city=""
password=""
cname=""
branch=""
stream=""
role=""
proof=""
describe=""
#login
em=''
pwd=''
#upload_blog
title=""
author=""
content=""
date=""
image=""
#upload_book
Bookn=""
seller=""
number=""
price=""
describe=""
stream=""
series=""

def register(request):
    error=""
    global name,email,blog,contact,country,city,password,cname,branch,stream,role,proof,describe
    
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        blog=request.POST['blog']
        contact=request.POST['contact']
        country=request.POST['country']
        city=request.POST['city']
        password=request.POST['password']
        cname=request.POST['college-name']
        branch=request.POST['branch']
        stream=request.POST['study-stream']
        role=request.POST['role']
        proof=request.POST['upload-proof']
        describe=request.POST['describe-yourself']

        try:
            Register.objects.create(name=name,email=email,blogurl=blog,contact=contact,country=country,city=city,password=password,collegename=cname,branch=branch,stream=stream,role=role,proof=proof,discribe=describe)

            error="No"

        except:
            error="Yes"
        m=sql.connect(host="localhost",port=30222, user="root", password="1234", database="ecom")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():

            if key == "name":
                name = value
            if key == "email":
                email = value 
            if key == "password":
                password = value
                  

        c = "insert into books (name,email,pasword) values('{}','{}','{}')".format(
            name,email,password)
        cursor.execute(c)
        m.commit()
           
    d={'error':error}        
    return render(request,"register.html",d)

def login(request):
    global em,pwd
    if request.method=='POST':
        m =sql.connect(host="localhost",port=30222, user="root", password="1234", database="ecom")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="password":
                pwd=value
            if key=="email":
                em=value    
        c="select * from books where   pasword='{}' and Email='{}'".format(pwd,em)
        cursor.execute(c)
        t=tuple(cursor.fetchall())   
        if t==():
            return render(request,'error.html')    
        else:
            request.session['username']=em
            print(em)
            #return redirect('home')
            return render(request,'index.html',{'data':em})
    return render(request,'login.html')
def index(request):
    #print("View accessed")
    #products = BookItem.objects.all()
    #print(products)
    return render(request,"index.html")

def blog(request):
    # Query the database to get all blog posts
    blog_posts =uploadblog.objects.filter(email__contains=str(request.session['username']))
    print(blog_posts)

    # Pass the blog_posts queryset to the template context
    blogs = {'blog_posts': blog_posts}
    
    # Render the blog.html template with the context data
    return render(request,'view_blog.html',blogs)


def view_books(request):
    # Fetch all book records from the database
    books = BookItem.objects.filter(email__contains=str(request.session['username']))

    # Render the template with the book data
    return render(request, 'view_books.html', {'books': books})
def all_books(request):
    books=BookItem.objects.all()
    return render(request, 'allbooks.html', {'books': books})
def home(request):
    main_blogs = mainblog.objects.all()
    print(blogs)
    return render(request, 'home.html', {'main_blogs': main_blogs})
def upload_blog(request):
    error=""
    if request.method == 'POST':
        # Manual form data retrieval
        email=request.POST.get("email")
        title = request.POST.get("title")
        authorname = request.POST.get("authorname")
        link = request.POST.get("link")
        ukey=extract_keywords_from_url(link)
        description = request.POST.get("description")
        dkey= extract_keywords(description)
        stream = request.POST.get("stream")

        try:

        # Create and save new UploadBlog instance
           uploadblog.objects.create(email=email,title=title, authorname=authorname, link=link,ukey=ukey,description=description,dkey=dkey, stream=stream)
           error="No"
        except:
            error="Yes"
        return render(request,"index.html")    
    d={'error':error}        
    return render(request, 'upload_blog.html',d)

#def payment(request):
   # return render(request,'payment.html')

#search bar functionality
import spacy
from urllib.parse import urlparse

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text)
    keywords = [token.text for token in doc if token.is_stop != True and token.is_punct != True]
    return " ".join(keywords)

def parse_url(url):
    parsed_url = urlparse(url)
    return {
        'scheme': parsed_url.scheme,
        'netloc': parsed_url.netloc,
        'path': parsed_url.path,
        'params': parsed_url.params,
        'query': parsed_url.query,
        'fragment': parsed_url.fragment
    }

def search_result(request):
    #print('search result ')
    if request.method == 'GET':
        #print("hello")
        query = request.GET.get('query','')
        #print(query)
        
        key =mainblog.objects.filter(dkey__contains=str(query))

        return render(request, 'search.html', {'key':key})
    return render(request, 'home.html')

import spacy
import pandas as pd
from urllib.parse import urlparse
import re


def extract_keywords_from_url(url):
    # Parse the URL
    parsed_url = urlparse(url)

    # Extract keywords from different components of the URL
    url_keywords = []

    # Extract keywords from the path
    path_keywords = re.findall(r'\w+', parsed_url.path)
    url_keywords.extend(path_keywords)

    # Extract keywords from query parameters
    # query_keywords = re.findall(r'\w+', parsed_url.query)
    # url_keywords.extend(query_keywords)

    # Extract keywords from fragments
    fragment_keywords = re.findall(r'\w+', parsed_url.fragment)
    url_keywords.extend(fragment_keywords)

    # Filter out short words
    url_keywords = [word.lower() for word in url_keywords if len(word) > 2]

    return ', '.join(url_keywords)



def uploadbook(request):
    error = ""
    
    if request.method == 'POST':
        name = request.POST['title']
        email = request.POST['email']
        price = request.POST['price']
        describe = request.POST['content']
        image = request.POST['image']

        try:
            BookItem.objects.create(name=name, email=email,price=price,description=describe,image=image)
            error = "No"
        except Exception as e:
            error = str(e)
        return render(request,"index.html") 
    context = {'error': error}
    return render(request, "upload_book.html", context)

#Customer Functions
def customer(request):
    error=""
    if request.method == 'POST':
       book_name = request.POST['Bookname']
       email = request.POST['email']
       phone=request.POST['Phone']
       full_name = request.POST['Full_Name']
       address_line1 = request.POST['Address_Line']
       city = request.POST['City']
       state = request.POST['State']
       postal_code = request.POST['Postal_Code']
       country = request.POST['Country']

       try:

        # Create and save new UploadBlog instance
            Customer.objects.create(book_name=book_name,email=email,phone=phone,full_name=full_name,address_line1=address_line1,city=city,state=state,postal_code=postal_code,country=country)
            error="No"
       except:
            error="Yes"
       return render(request,'thank.html')    
    d={'error':error}        
    return render(request, 'payment.html',d)
def thank(request):
    return render(request,'thank.html')