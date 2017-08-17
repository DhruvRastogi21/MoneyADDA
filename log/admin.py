# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import AccountHolder,Transaction

admin.site.register(AccountHolder)
admin.site.register(Transaction)
