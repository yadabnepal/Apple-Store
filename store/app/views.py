from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import AuthenticationForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm

from django.contrib.auth.decorators import user_passes_test

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from app.models import *




from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist


from django.db.models import Q
# Create your views here.

def home_fn(request):
	getiphone = products.objects.all().order_by('-id')[:6]
	return render(request, 'app/home.html', {'iphone':getiphone})
	
def viewall_fn(request):
	getiphone = products.objects.all().order_by('-id')
	return render(request, 'app/viewallproducts.html', {'iphone':getiphone})
	
def message_fn(request):
	return render(request,'app/message.html')

def aboutus_fn(request):
	return render(request,'app/aboutus.html')
	
	
def passdone_fn(request):
	return render(request,'app/password_reset/password_reset_done.html')
	
def passcomplete_fn(request):
	return render(request,'app/password_reset/password_reset_complete.html')
	
def thanks(request):
    return render(request,'app/contact_us/thanks.html')

def privacy_fn(request):
    return render(request,'app/privacy_policy.html')
	
def term_fn(request):
    return render(request,'app/term.html')
	
def reg_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		if(User.objects.filter(username=username).exists()):
			messages.info(request, 'Username is already registered')
			return render(request,'app/register.html')
		password = request.POST.get('password')
		email = request.POST.get('email')
		first_name = request.POST.get('fname')
		last_name = request.POST.get('lname')
		user = User(first_name = first_name,
				last_name = last_name,
				username = username,
				password = password,
				email = email
				)
		user.set_password(password)		
		user.save()
		return HttpResponseRedirect(reverse('app.views.message_fn'), messages.info(request, 'User is successfully registered'))
	return render(request,'app/register.html')
	
def login_user(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	
	user = authenticate(username = username, password = password)
	if request.user.is_active: 
		return HttpResponseRedirect(reverse('app.views.message_fn'), messages.error(request, 'You are already logged in'))
	if request.method == 'POST':
		if user is not None:
			if user.is_active :
				login(request, user)
				if request.user.is_staff: 
					return HttpResponseRedirect(reverse('app.views.adminpanel_fn'))
				return HttpResponseRedirect("/home/")
		
			else:
				return HttpResponse("User account is disabled")
		else:
				messages.error(request, 'Invalid Username or Password')
				return HttpResponseRedirect("/login")
	return render(request, 'app/login.html')
	
def logout_user(request):
	logout(request)
	return HttpResponseRedirect("/home/")
	
def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='app/password_reset/password_reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect=reverse('app:password_reset_complete'))
	

def reset(request):
    return password_reset(request, template_name='app/password_reset/password_reset_form.html',
        email_template_name='app/password_reset/password_reset_email.txt',
        subject_template_name='app/password_reset/resetsub.txt',
        post_reset_redirect=reverse('app:password_reset_done'))
		
		
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email'),
                ['samipnepal@gmail.com'], #email address where message is sent.
            )
            return HttpResponseRedirect('/thanks/')
    return render(request, 'app/contact_us/contact.html', {'errors': errors})
		


def iphone_upload(request):
	if not request.user.is_staff: 
		messages.error(request, 'Only super user is allowed')
		return render(request,'app/login.html')
	if request.method=='POST':
		product = request.POST.get('product')
		model = request.POST.get('model')
		color = request.POST.get('color')
		size = request.POST.get('size')
		price = request.POST.get('price')
		details = request.POST['details']
		photo = request.FILES['photo']
		ip=products(product=product,model=model,color=color,size=size,price=price,photo=photo,details=details)
		ip.save()
		messages.info(request, 'Successfully added to database')
		return HttpResponseRedirect(reverse('app.views.productlist_fn'))
	return render(request,'app/admin_panel/iphone_upload.html')

def productlist_fn(request):
	if request.user.is_staff:
		retrieve = products.objects.all()
		return render(request, 'app/admin_panel/product_list.html', {'getphoto':retrieve})
	messages.error(request, 'Only For Staff')
	return HttpResponseRedirect(reverse('app.views.message_fn'))
	
def userlist_fn(request):
	retrieve = User.objects.all()
	return render(request, 'app/admin_panel/user_list.html', {'getphoto':retrieve})

def deleteuser(request, id):
	note = get_object_or_404(User, pk=id).delete()
	retrieve = User.objects.all()
	messages.info(request, 'User Deleted Successfully')
	return render(request, 'app/admin_panel/user_list.html', {'getphoto':retrieve})
	
	
def iphone_listfn(request):
	retrieves = products.objects.filter(Q(product__icontains='iphone'))
	prod = products.objects.filter(product='iPhone')[:1]
	return render(request, 'app/products.html', {'getphotos':retrieves, 'get':prod})

def macbook_listfn(request):
	retrieves = products.objects.filter(Q(product__icontains='macbook'))
	prod = products.objects.filter(product='Macbook')[:1]
	return render(request, 'app/products.html', {'getphotos':retrieves, 'get':prod})

def ipod_listfn(request):
	retrieves = products.objects.filter(Q(product__icontains='ipod'))
	prod = products.objects.filter(product='iPod')[:1]
	return render(request, 'app/products.html', {'getphotos':retrieves, 'get':prod})
	
def ipad_listfn(request):
	retrieves = products.objects.filter(Q(product__icontains='ipad'))
	prod = products.objects.filter(product='iPad')[:1]
	return render(request, 'app/products.html', {'getphotos':retrieves, 'get':prod})

def prodetail(request, id):
	retrieves = products.objects.get(id=id) 
	com = comments.objects.filter(productid=id).order_by('-id')[:4]
	return render(request, 'app/product_details.html', {'photos':retrieves, 'comments':com})
	
def delete(request, id):
    note = get_object_or_404(products, pk=id).delete()
    return HttpResponseRedirect(reverse('app.views.productlist_fn'), messages.info(request, 'Successfully Deleted'))
	
def search_fn(request):
	if request.method == 'POST':
		item = request.POST.get('search')
		if products.objects.filter(Q(product__icontains = item)).exists():
			getiphone = products.objects.filter(Q(product__icontains = item))
			return render(request, 'app/search_result.html', {'iphone':getiphone})
		if products.objects.filter(Q(model__icontains = item)).exists():
			getiphone = products.objects.filter(Q(model__icontains = item))
			return render(request, 'app/search_result.html', {'iphone':getiphone})
		if products.objects.filter(Q(size__icontains = item)).exists():
			getiphone = products.objects.filter(Q(size__icontains = item))
			return render(request, 'app/search_result.html', {'iphone':getiphone})
		if products.objects.filter(Q(color__icontains = item)).exists():
			getiphone = products.objects.filter(Q(color__icontains = item))
			return render(request, 'app/search_result.html', {'iphone':getiphone})
		messages.info(request, 'Result not found')
		return render(request,'app/message.html')
	return render(request, 'app/search_result.html')


def payment(request, id):
	from datetime import datetime
	if request.method == 'POST':
		productid=request.POST.get('productid')
		prodmodel=request.POST.get('productmodel')
		username=request.POST.get('username')
		prodcolor=request.POST.get('prodcolor')
		prodsize=request.POST.get('prodsize')
		prodprice=request.POST.get('prodprice')
		cardtype=request.POST.get('cardtype')
		cardnumber=request.POST.get('cardnumber')
		expiryyear=request.POST.get('expiryyear')
		expirymonth=request.POST.get('expirymonth')
		cvv=request.POST.get('cvv')
		cardname=request.POST.get('cardname')
		country=request.POST.get('country')
		address1=request.POST.get('address1')
		address2=request.POST.get('address2')
		city=request.POST.get('city')
		state=request.POST.get('state')
		postalcode=request.POST.get('postalcode')
		phonenumber=request.POST.get('phonenumber')
		email=request.POST.get('email')
		userid=request.POST.get('userid')
		date = datetime.now()
		status='Pending'
		upload=payments(productid=productid,prodmodel=prodmodel,username=username,prodcolor=prodcolor,prodsize=prodsize,prodprice=prodprice,cardtype=cardtype,cardnumber=cardnumber,expiryyear=expiryyear,expirymonth=expirymonth,cvv=cvv,cardname=cardname,country=country,address1=address1,address2=address2,city=city,state=state,postalcode=postalcode,phonenumber=phonenumber,email=email,userid=userid,status=status,date=date)
		t=open("c:/project/env/store/app/templates/app/paymentmail.txt")
		sub=t.read()
		uemail=User.objects.get(id=userid)
		if request.user.is_active:
			send_mail(
                'Order Confirmation for ' + prodmodel,
                'Congratulation!!! '+uemail.first_name+sub,
                'mail@anedia.com',
                [uemail.email], #email address where message is sent.
            )
		upload.save()
		messages.info(request, 'Payment Is Successfully Placed')
		return HttpResponseRedirect(reverse('app.views.message_fn'))
	retrieves = products.objects.get(id=id)
	return render(request, 'app/payment.html', {'product':retrieves})

@login_required(login_url = '/login/')
def userprofile_fn(request, id):
	user = User.objects.get(id=id)
	if userprofiles.objects.filter(userid=id).exists():
		retrieves = get_object_or_404(userprofiles, userid=id)
		return render(request, 'app/user_profile.html', {'users':retrieves, 'acc':user})
	return render(request, 'app/user_profile.html', {'acc':user})



@login_required(login_url = '/login/')
def userprofileupdate_fn(request, id):
	if request.method == 'POST':
		userid=request.POST.get('userid')
		day=request.POST.get('day')
		month=request.POST.get('month')
		year=request.POST.get('year')
		dob=year+"-"+month+"-"+day
		country=request.POST.get('country')
		state=request.POST.get('state')
		city=request.POST.get('city')
		phone=request.POST.get('phone')
		mobile=request.POST.get('mobile')
		gender=request.POST.get('gender')
		userphoto = request.FILES['userphoto']
		try:
			profile = userprofiles.objects.get(userid=id)
			profile.userid = userid
			profile.dob = dob
			profile.country = country
			profile.state= state
			profile.city = city
			profile.phone = phone
			profile.mobile = mobile
			profile.gender = gender
			profile.userphoto = userphoto
			profile.save()
			messages.info(request, 'Profile Updated Successfully')
			return HttpResponseRedirect(reverse('app.views.message_fn'))
		except (ValueError, ObjectDoesNotExist):
			upload=userprofiles(userid=userid,dob=dob,country=country,state=state,city=city,phone=phone,mobile=mobile,gender=gender,userphoto=userphoto)
			upload.save()
			messages.info(request, 'Profile Updated')
			return HttpResponseRedirect(reverse('app.views.message_fn'))
	if userprofiles.objects.filter(userid=id).exists():
		retrieves = get_object_or_404(userprofiles, userid=id)
		return render(request,'app/userprofileupdate.html', {'profile':retrieves})
	return render(request,'app/userprofileupdate.html')


@login_required(login_url = '/login/')
def adminpanel_fn(request):
	if request.user.is_staff: 
		return render(request,'app/admin_panel/adminpanel.html')
	messages.info(request, 'Only For Staff')
	return render(request,'app/message.html')

@login_required(login_url = '/login/')
def vieworders_fn(request, id):
	if payments.objects.filter(userid=id).exists():
		retrieves = payments.objects.filter(userid=id)
		return render(request, 'app/view_orders.html', {'photos':retrieves})
	messages.info(request, 'You have no order')
	return HttpResponseRedirect(reverse('app.views.message_fn'))

@login_required(login_url = '/login/')
def orderlist_fn(request):
	if request.user.is_staff: 
		retrieves = payments.objects.all()
		return render(request,'app/admin_panel/order_list.html', {'photos':retrieves})
	messages.info(request, 'Only For Staff')
	return render(request,'app/message.html')

def ordercancel(request, id):
    note = get_object_or_404(payments, pk=id).delete()
    return HttpResponseRedirect(reverse('app.views.message_fn'), messages.info(request, 'Your Order Has Been Canceled'))
	
def statuschange_fn(request, id):
	note = get_object_or_404(payments,id=id)
	if note.status =='Pending':
		note.status='Delivered'
		note.save()
		return HttpResponseRedirect(reverse('app.views.orderlist_fn'), messages.info(request, 'Order Has Been Delivered'))
	note.status='Pending'
	note.save()
	return HttpResponseRedirect(reverse('app.views.orderlist_fn'), messages.info(request, 'Status has been changed to Pending'))


@login_required(login_url = '/login/')
def orderbydelivery(request):
	note = payments.objects.filter(status='Pending')
	return render(request,'app/admin_panel/order_list.html', {'photos':note})

@login_required(login_url = '/login/')
def orderbyuser(request, id):
	note = payments.objects.filter(userid=id)
	return render(request,'app/admin_panel/order_list.html', {'photos':note})

import datetime
@login_required(login_url = '/login/')
def orderbytodaydate(request):
	today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
	today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
	note = payments.objects.filter(date__range=(today_min, today_max))
	return render(request,'app/admin_panel/order_list.html', {'photos':note})


@login_required(login_url = '/login/')
def orderbyweekdate(request):
	date = datetime.date.today()
	start_week = date - datetime.timedelta(date.weekday())
	end_week = start_week + datetime.timedelta(7)
	note = payments.objects.filter(date__range=[start_week, end_week])
	return render(request,'app/admin_panel/order_list.html', {'photos':note})


@login_required(login_url = '/login/')
def orderbymonthdate(request):
	start_of_month = datetime.date.today().replace(day=1)
	note = payments.objects.filter(date__gte=start_of_month)
	return render(request,'app/admin_panel/order_list.html', {'photos':note})	

def comments_fn(request):
	if request.method == 'POST':
		comment = request.POST.get('comment')
		userid = request.POST.get('userid')
		productid = request.POST.get('productid')
		username = request.POST.get('username')
		post = comments(userid=userid,productid=productid,username=username,comment=comment)
		post.save()
		request.session['id'] = productid
		return HttpResponseRedirect(reverse('app.views.prodetail_fn'), messages.info(request, 'Your review has been posted successfully'))

def prodetail_fn(request):
	id = request.session.get('id')
	retrieves = products.objects.get(id=id)
	com = comments.objects.filter(productid=id).order_by('-id')[:4]
	return render(request, 'app/product_details.html', {'photos':retrieves, 'comments':com})
	

def deletecomment(request, id):
	proid = comments.objects.get(id=id)
	request.session['id'] = proid.productid
	note = get_object_or_404(comments, pk=id).delete()
	return HttpResponseRedirect(reverse('app.views.prodetail_fn'), messages.info(request, 'Comment Successfully Deleted'))

@login_required(login_url = '/login/')
def change_password(request, id):
	if request.method == 'POST':
		newpass = request.POST.get('password')
		user = User.objects.get(id=id)
		user.set_password(newpass)
		user.save()
		messages.info(request, 'Password Changed Successfully')
		return render(request, 'app/message.html')
	return render(request, 'app/change_password.html')