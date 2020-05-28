from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from register.models import User
from register.forms import DataForm, KannadaDataForm, HindiDataForm, TextForm
from .models import Data
from django.core.exceptions import ValidationError


def index(request):
    return render(request, 'register/index.html')


def success(request):
    if request.method == 'POST':
        myForm = DataForm(request.POST, request.FILES)

        if myForm.is_valid():

            text = myForm.cleaned_data['text']
            category = myForm.cleaned_data['category']
            upload = myForm.cleaned_data['upload']
            extension = str(upload).split('.')[1].lower()
            if category == 'Text':
                if extension not in ['txt', 'csv', 'pdf', 'doc']:
                    return HttpResponse("Only Text Files are allowed")
            elif category == 'Image':
                if extension not in ['png', 'jpeg', 'jpg']:
                    return HttpResponse("Only Image Files are allowed")
            elif category == 'Audio':
                if extension not in ['mp3', 'dat']:
                    return HttpResponse("Only Audio Files are allowed")
            elif category == 'Video':
                if extension not in ['avi', 'mp4', '3gp', 'mov', 'mkv']:
                    return HttpResponse("Only Video Files are allowed")

            data = Data(
                text=text,
                category=category,
                upload=upload
            )
            data.save()
            return HttpResponse("Data uploaded succesfully")
        else:
            print(myForm)
            return HttpResponse("Invalid data in the form")
    else:
        form = DataForm()
        return render(request, 'index.html', {'form': form})


def success_kannada(request):
    if request.method == 'POST':
        myForm = KannadaDataForm(request.POST, request.FILES)

        if myForm.is_valid():
            text = myForm.cleaned_data['text']
            category = myForm.cleaned_data['category']
            upload = myForm.cleaned_data['upload']
            extension = str(upload).split('.')[1].lower()
            if category == 'Text':
                if extension not in ['txt', 'csv', 'pdf', 'doc']:
                    return HttpResponse("Only Text Files are allowed")
            elif category == 'Image':
                if extension not in ['png', 'jpeg', 'jpg']:
                    return HttpResponse("Only Image Files are allowed")
            elif category == 'Audio':
                if extension not in ['mp3', 'dat']:
                    return HttpResponse("Only Audio Files are allowed")
            elif category == 'Video':
                if extension not in ['avi', 'mp4', '3gp', 'mov', 'mkv']:
                    return HttpResponse("Only Video Files are allowed")
            data = Data(
                text=text,
                category=category,
                upload=upload
            )
            data.save()
            return HttpResponse('&#3233;&#3262;&#3231;&#3253;&#3240;&#3277;&#3240;&#3265; &#3247;&#3254;&#3256;&#3277;&#3253;&#3263;&#3247;&#3262;&#3223;&#3263; &#3205;&#3242;&#3277;&#3250;&#3275;&#3233;&#3277; &#3246;&#3262;&#3233;&#3250;&#3262;&#3223;&#3263;&#3238;&#3270;')
        else:
            print(myForm)
            return HttpResponse("&#3248;&#3266;&#3242;&#3238;&#3250;&#3277;&#3250;&#3263; &#3205;&#3246;&#3262;&#3240;&#3277;&#3247; &#3233;&#3262;&#3231;")
    else:
        form = KannadaDataForm()
        return render(request, 'register/kannada.html', {'form': form})


def success_hindi(request):
    if request.method == 'POST':
        myForm = HindiDataForm(request.POST, request.FILES)

        if myForm.is_valid():

            text = myForm.cleaned_data['text']
            category = myForm.cleaned_data['category']
            upload = myForm.cleaned_data['upload']
            extension = str(upload).split('.')[1].lower()
            if category == 'Text':
                if extension not in ['txt', 'csv', 'pdf', 'doc']:
                    return HttpResponse("Only Text Files are allowed")
            elif category == 'Image':
                if extension not in ['png', 'jpeg', 'jpg']:
                    return HttpResponse("Only Image Files are allowed")
            elif category == 'Audio':
                if extension not in ['mp3', 'dat']:
                    return HttpResponse("Only Audio Files are allowed")
            elif category == 'Video':
                if extension not in ['avi', 'mp4', '3gp', 'mov', 'mkv']:
                    return HttpResponse("Only Video Files are allowed")
            data = Data(

                text=text,
                category=category,
                upload=upload
            )
            data.save()
            return HttpResponse('&#3233;&#3262;&#3231;&#3253;&#3240;&#3277;&#3240;&#3265; &#3247;&#3254;&#3256;&#3277;&#3253;&#3263;&#3247;&#3262;&#3223;&#3263; &#3205;&#3242;&#3277;&#3250;&#3275;&#3233;&#3277; &#3246;&#3262;&#3233;&#3250;&#3262;&#3223;&#3263;&#3238;&#3270;')
        else:
            print(myForm)
            return HttpResponse("&#3248;&#3266;&#3242;&#3238;&#3250;&#3277;&#3250;&#3263; &#3205;&#3246;&#3262;&#3240;&#3277;&#3247; &#3233;&#3262;&#3231;")
    else:
        form = HindiDataForm()
        return render(request, 'register/hindi.html', {'form': form})


def register(request):
    if request.method == 'POST':
        errors = User.objects.validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')

        # hashed_password = bcrypt.(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                                   password=request.POST['password'], email=request.POST['email'])
        user.save()
        request.session['id'] = user.id
        return redirect('/success')
    else:
        return render(request, 'register/register.html', {})


def login(request):
    if request.method == 'POST':
        if User.objects.filter(email=request.POST['login_email']).exists():
            user = User.objects.filter(email=request.POST['login_email'])[0]
            # if bcrypt.checkpw(request.POST['login_password'].encode('utf-8'), user.password.encode('utf-8')):
            if user.password == request.POST['login_password']:
                request.session['id'] = user.id
                return redirect('/success')
        return redirect('/')
    else:
        return render(request, 'register/index.html', {})


def get_related_text(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            all_related_texts = []
            text = form.cleaned_data['text']
            if len(text) >= 0:
                data_objects = Data.objects.all()
                for data in data_objects:
                    cur_sentence = data.text
                    if cur_sentence[0] == text[-1]:
                        all_related_texts.append(cur_sentence)
            form = TextForm()
            return render(request, 'register/get_related_text.html', {
                'form': form,
                'data': all_related_texts
            })
        else:
            return HttpResponse("Wrong Data")

    else:
        form = TextForm()
        return render(request, 'register/get_related_text.html', {
            'form': form
        })
