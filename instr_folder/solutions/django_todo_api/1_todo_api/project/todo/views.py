import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Profile, Todos
from django.views.generic import View
from django.shortcuts import get_object_or_404

# Create your views here.

class Register(View):
	def post(self, request):
		body_unicode = request.body.decode('utf-8')
		content = json.loads(body_unicode)

		user = User.objects.create_user(content.get('username'), password=content.get('password'))

		# user = User(username = content.get('username'), password=content.get('password'))
		# user.save()

		profile = Profile.objects.create(name = user)
		
		user.save()
		return JsonResponse({'user':profile.token.hex})

class LoginView(View):
	def post(self,request):
		body_unicode = request.body.decode('utf-8')
		content = json.loads(body_unicode)
		username = content.get('username')
		password = content.get('password')
		user = authenticate(username=username, password=password)
		if user:
			return JsonResponse({'token': user.profile.token.hex})
		else:
			return JsonResponse({'response': 'Does not exist'})

class CreateTodo(View):
	def post(self,request, token):
		body_unicode = request.body.decode('utf-8')
		content = json.loads(body_unicode)
		profile = get_object_or_404(Profile, token=token)
		todo = Todos.objects.create(user_id = profile,content = content.get('content'))
		todo.save()
		return JsonResponse({"message": "Created"})

class ViewAll(View):
	def get(self, request, token):
		profile = get_object_or_404(Profile, token=token)
		todo_object = profile.todos_set.all()
		todo = [todo.to_json() for todo in todo_object ]
		return JsonResponse(todo)

class ViewUnfinished(View):
	def get(self, request, token):
		profile = get_object_or_404(Profile, token=token)
	
		unfinished_todos = profile.todos_set.filter(finished = False)
		response = [todo.to_json() for todo in unfinished_todos ]
		if not response:
			response = {"message": "No unfinished todos"}
		return JsonResponse(response)


