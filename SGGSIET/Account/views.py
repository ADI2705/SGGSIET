from django.shortcuts import render
from .models import Account

def Account_list(request):
    Accounts = Account.objects.all()
    return render(request, 'Account/Account_list.html', {'Account': Accounts})

def Account_detail(request, Account_id):
    Account = Account.objects.get(id=Account_id)
    # Add additional logic if needed
    return render(request, 'Account/Account_detail.html', {'Account': Account})
