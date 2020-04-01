from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Artists, Songs, Ratings
from .forms import SongInput, ArtistInput, RatingInput
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def home(request):
	a = Ratings.objects.raw('select s.id,s.cover, s.song_name, round(avg(r.rating), 1) rate from myapp_ratings r, myapp_songs s where r.song_id = s.id group by r.song_id order by rate desc limit 10')
	song = {}
	img = {}
	artist_name = {}
	for i in a:
		b = Artists.objects.raw('select sa.id, a.artist_name from myapp_artists a join myapp_songs_artist sa on sa.artists_id = a.id where sa.songs_id ='+str(i.id))
		sub = ""
		for j in b:
			sub += " "+j.artist_name
		artist_name[i.song_name] = sub
		song[i.song_name] = [float(i.rate), i.cover,sub]

	s = "SELECT A.id, A.ARTIST_NAME, ROUND(AVG(R.RATING), 1) Rating FROM myapp_artists A INNER JOIN myapp_songs_artist RE ON A.ID = RE.ARTISTS_ID INNER JOIN myapp_ratings R ON RE.SONGS_ID = R.SONG_ID GROUP BY (RE.ARTISTS_ID) ORDER BY Rating DESC limit 10"
	b = Artists.objects.raw(s)
	artist = {}
	for j in b:
		artist[j.artist_name] = j.Rating

	data = {
		'song_ratings' : song,
		'artist_ratings': artist,
		'artist_name': artist_name
	}
	return render(request,"home.html", data)

def add(request):
	form = SongInput()

	if request.method == 'POST':
		form = SongInput(request.POST, request.FILES)

		if form.is_valid():
			form.save(commit = True)
			return home(request)
		else:
			print("hello")

	return render(request, "add.html", {"form": form})


def art(request):
	form = ArtistInput()

	if request.method == 'POST':
		form = ArtistInput(request.POST)

		if form.is_valid():
			form.save(commit = True)

			return home(request)

	return render(request, "art.html", {"form": form})

def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username = username, password = password)

	if user:
		auth.login(request, user)
		return redirect('/')
	else:
		messages.info(request, "Invalid Credentials")
		return redirect('/')

	return home(request)

def signup(request):
	if request.method == 'POST':

		username = request.POST['username']
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		email = request.POST['email']
		pass1 = request.POST['password1']
		pass2 = request.POST['password2']

		if pass1 == pass2:
			if User.objects.filter(username = username).exists():
				messages.info(request, "username already taken")
				return redirect('signup')
			elif User.objects.filter(email = email).exists():
				messages.info(request, "email already taken")
				return redirect('signup')
			else:
				user = User.objects.create_user(username = username, password = pass1, email = email, first_name = firstname, last_name = lastname)
				user.save()
				messages.info(request, "user created")
		else:
			messages.info(request, "passwords not matching")
			return redirect('signup')
	return redirect('/')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('/')

def rating(request):
		form = RatingInput()

		if request.method == 'POST':
			form = RatingInput(request.POST)
			if form.is_valid():
				form.save(commit = True)
				return home(request)

		return render(request, "rating.html", {"form": form})
