#log/views.py
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import AccountHolder,Transaction
from .forms import TransactionForm
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
            u1 = User.objects.get(username=t.username_of_recipient)
            u2=User.objects.get(username=request.user)
            c=CurrencyRates()
            t.amount=form.cleaned_data['amount']
            if t.currency==u1.accountholder.currency:
                u1.accountholder.Acc_balance +=t.amount
            else:
                u1.accountholder.Acc_balance+=c.convert(t.currency,u1.accountholder.currency,t.amount)
            if t.currency==u2.accountholder.currency:
                u2.accountholder.Acc_balance-=t.amount
            else:
                u2.accountholder.Acc_balance -= c.convert(t.currency, u2.accountholder.currency, t.amount)

            u1.accountholder.save()
            u2.accountholder.save()

            t.save()

            return redirect('home')
    else:
        form=TransactionForm()
    return render(request,'transaction_form.html',{'form':form,'f_name':f_name})