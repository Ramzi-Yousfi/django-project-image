import json
from django.shortcuts import render
from django.http import HttpResponse
import os
from pathlib import Path

def index(request):
    base_dir = Path(__file__).parent.parent
    path_json = Path(base_dir /'books.json')
    with open(path_json, 'r') as f:
        books = json.load(f)
    return render(request, 'index.html', {'books': books})
     

def two(request):
    return HttpResponse("Hello, world. You're at the books two.")