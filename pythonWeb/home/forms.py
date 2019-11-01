from django import forms 
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.forms.widgets import DateTimeInput, DateInput 
import sqlite3
from .functions import generateInsertCommand


class CusFormSea(forms.Form):
    #id = forms.IntegerField()
    pc_collection = forms.CharField(max_length=100)
    collection_address = forms.CharField(max_length=200)
    consignee = forms.CharField(max_length=300)
    commodity = forms.CharField(max_length=300)
    detail_of_package = forms.CharField(max_length=300)
    type_way = forms.CharField(max_length=100)
    term = forms.CharField(max_length=100)
    po_no = forms.CharField(max_length=200)
    co_by_forwarder= forms.CharField(max_length=300)
    packing_by_forwarder= forms.CharField(max_length=300)
    hazardous_yes_no= forms.CharField(max_length=300)
    date_request = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    deadline_pickup  = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    deadline_bill  = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    deadline_available  = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))

    def save(self):                         # định nghĩa hàm save(self) kiểm tra có dữ liệu trong các trường chưa
        print(self.cleaned_data["pc_collection"])
        print(self.cleaned_data["collection_address"])
        return None




