from django.shortcuts import render, redirect
from pytube import YouTube
import urllib.request
import urllib.parse
import re
import os
# Create your views here.
def home(request):
    try:
        prev= request.POST['hidden']
        print("success")
        if os.path.exists(os.path.join("C:/Users/Rohit/OneDrive/New folder (4)/vll/medias", str(prev)+".mp4")):
            print("path found")
            os.remove(os.path.join("C:/Users/Rohit/OneDrive/New folder (4)/vll/medias", str(prev)+".mp4"))
            print("removed")
    except:
        pass
    try:
        username = request.POST['song']
        query_string = urllib.parse.urlencode({"search_query" : username})
        print(query_string)
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'/watch\?v=(.{11})', html_content.read().decode())
        input2 = "http://www.youtube.com/watch?v=" + search_results[0]
        Video = YouTube(input2)
        Video.streams.filter(only_audio=True).first().download(output_path="C:/Users/Rohit/OneDrive/New folder (4)/vll/medias", filename=username)
        thumbnail = Video.thumbnail_url
        print("loded")
        return render(request, 'main.html', {"link":thumbnail, "name1": username.upper(), "name2": username})
    except:
        return redirect('/home')
def home1(request):
    return render(request, template_name="temp.html")