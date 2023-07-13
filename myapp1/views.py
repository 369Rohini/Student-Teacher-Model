from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'base.html')

def about(request):
    return HttpResponse('this is aboutpage')

def user_register(request):
    return HttpResponse('ths is register page')

def login(request):
    return render(request,'login.html')

def Signup(request):
    return render(request,'signup.html')




def Teacher(request):
    data={}
    output=0
    try:
        if request.method=="POST":
            name=str(request.POST.get('name'))
            msg=str(request.POST.get('msg'))
            output= (name + " \n "  + msg)
            

    except:
        pass
    return render(request,"Teacher.html",{'result':output})

# def Teacher(request):
#     finalans=0
#     data={}
#     try:
#         if request.method=="POST":
#             name=str(request.POST.get('name'))
#             msg=str(request.POST.get('msg'))
#             finalans= (name + " \n "  + msg)
#             data={
#                 'name':name,
#                 'msg':msg,
#                 'output':finalans

#             }

#             url="/Student/?output={}".format(finalans)
#             return HttpResponseRedirect(url)
#     except:
#         pass
#     return render(request,"Teacher.html",data)


# def Student(request):
#     if request.method=="POST":
#         name=request.POST.get("name")
#         msg=request.POST.get("take_msg")
#         # display_msg=print(name,msg)
#         user= User.objects.create_user(name=name,take_msg=msg)
#         user.save()
#         redirect('Student')
#     return render(request,"Teacher.html",{'result':display_msg})
        
# def Student(request):
#     if request.method =='GET':
#         output=request.GET.get('output')
#     return render(request,"Student.html",{'output':output})



# def thank(request):
#     if request.method=='GET':
#         output=request.GET.get('output')

#     return render(request,"thank.html",{'output':output})


# # this is my logic ---------------------->
# def userForm(request):
#     finalans=0
#     data={}
#     try:
#         if request.method=="POST":
#             n1=str(request.POST.get('num1'))
#             n2=str(request.POST.get('num2'))
#             finalans=(n1 + n2 + "hii")
#             data={
#                 'n1':n1,
#                 'n2':n2,
#                 'output':finalans
#             }
#             url="/thank/?output={}".format(finalans)
#             return HttpResponseRedirect(url)
#         # n1=int(request.GET['num1'])
#         # n2=int(request.GET['num2'])     
#     except:
#         pass
#     # return render(request,"userform.html",{'output':finalans})
#     return render(request,"userform.html",data)