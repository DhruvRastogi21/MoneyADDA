#log/views.py
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from .models import AccountHolder,Transaction
from .forms import TransactionForm,SignUpForm
from django.utils import timezone
from forex_python.converter import CurrencyRates

# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login")
def home(request):

    user=User.objects.get(username=request.user)
    f_name=user.first_name
    l_name=user.last_name
    bal=user.accountholder.Acc_balance
    curr=user.accountholder.currency
    context={'f_name':f_name,'l_name':l_name,'bal':bal,'curr':curr}



    return render(request,"home.html",context)

@login_required(login_url="login")
def new_transaction(request):
    user = User.objects.get(username=request.user)
    f_name = user.first_name



    if request.method=='POST':
        form = TransactionForm(request.POST)


        if form.is_valid():
            t = form.save(commit=False)
            t.debited_from=request.user
            t.date=timezone.now()
            username_of_recipient= User.objects.get(username=t.username_of_recipient)
            username_of_payer=User.objects.get(username=request.user)
            t.amount=form.cleaned_data['amount']
            username_of_payer.accountholder.debit(t.amount,t.currency)
            username_of_recipient.accountholder.credit(t.amount,t.currency)

            return redirect('home')
    else:
        form=TransactionForm()
    return render(request,'transaction_form.html',{'form':form,'f_name':f_name})

@login_required(login_url="login")
def details(request):
    user=User.objects.get(username=request.user)
    username=user.username
    f_name=user.first_name
    l_name=user.last_name
    balance=user.accountholder.Acc_balance
    date_of_birth=user.accountholder.date_of_birth
    currency=user.accountholder.currency
    context={'username':username,
    'f_name':user.first_name,
    'l_name':user.last_name,
    'balance':user.accountholder.Acc_balance,
    'date_of_birth':user.accountholder.date_of_birth,
    'currency':user.accountholder.currency}
    return render(request,'details.html',context)



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            accholder=AccountHolder()
            accholder.user=user
            accholder.save()
            user.accountholder.date_of_birth = form.cleaned_data.get('date_of_birth')
            user.accountholder.currency=form.cleaned_data.get('currency')
            user.save()
            user.accountholder.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
