import json
from django.shortcuts import render
from django.http import HttpResponse
import os
from pathlib import Path


base_dir = Path(__file__).parent.parent
path_json = Path(base_dir /'books.json')
with open(path_json, 'r') as f:
    books = json.load(f)

def index(request):
  
    return render(request, 'index.html', {'books': books})
     

def detail(request, book_id):
    base_dir = Path(__file__).parent.parent
    path_json = Path(base_dir /'books.json')
    with open(path_json, 'r') as f:
        books = json.load(f)
    book = books[book_id]
    return render(request, 'detail.html', {'book': book})