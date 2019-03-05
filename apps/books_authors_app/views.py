from django.shortcuts import render, redirect
from apps.books_authors_app.models import *

def book(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, "addBook.html", context)

def bookInfo(request, num):
    context = {
        "book": Book.objects.get(id=num),
        "authors": Author.objects.all(),
    }
    return render(request, "showBook.html", context)

def addBook(request):
    if len(request.POST['title']) < 2:
        print("Please enter a Full Title")
        return redirect('/')
    else:
        Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')

def linkAuth(request, num):
    this_book = Book.objects.get(id=num)
    this_author = Author.objects.get(id=int(request.POST['author']))
    this_book.author_id.add(this_author)
    print(this_author.first_name)
    return redirect("/books/"+num)

def author(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, "addAuthor.html", context)

def authInfo(request, num):
    context = {
        "author": Author.objects.get(id=num),
        "books": Book.objects.all()
    }
    return render(request, "showAuthor.html", context)

def addAuth(request):
    if len(request.POST['fname']) < 2:
        print("Please enter a first name")
        return redirect('/authors')
    if len(request.POST['lname']) < 2:
        print("Please enter a last name")
        return redirect('/authors')
    else:
        Author.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], notes=request.POST['note'])
    return redirect('/authors')

def linkBook(request, num):
    this_author = Author.objects.get(id=num)
    this_book = Book.objects.get(id=int(request.POST['book']))
    this_author.book_id.add(this_book)
    print(this_author.first_name)
    return redirect("/authors/"+num)