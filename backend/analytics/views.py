from django.shortcuts import render
from .models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
# Create your views here.
class RevenueStoreAPI(APIView):
    def post(self,request):
        data = request.data
        vendorId = data['vendorId']
        Response = {}
        order_objs = Order.objects.all(time__gte = datetime.datetime.now() - datetime.timedelta(days=30))
        net_revenue = 0.0
        revenue_list = []
        for order_obj in order_objs:
            inventory_id = order_obj.inventory
            inventory_obj = Inventory.objects.get(pk=inventory_id)
            order_inventory_objs = Order.objects.filter(inventory=inventory_obj)
            for order_inventory_obj in order_inventory_objs:
                product_id = order_obj.product
                product_obj = Product.objects.filter(pk=product_id)
                quantity = order_obj.quantity
                net_revenue =  net_revenue + product_obj.selling_price*quantity
                revenue_list['inventoryId'] = inventory_id
                revenue_list['netRevenue'] = net_revenue


        Response['status'] = 200
        Response['revenue_list'] = revenue_list
        return Response

class OrderStoreAPI(APIView):
    def post(self,request):
        data = request.data
        vendorId = data['vendorId']
        inventory_objs = Inventory.objects.filter(vendor=vendorId)
        Response = {}
        revenue_quantity = []
        for inventory_obj in inventory_objs:
            order_inventory_objs = Order.objects.filter(inventory=inventory_obj.id,time__gte = datetime.datetime.now() - datetime.timedelta(days=30))
            for order_inventory_obj in order_inventory_objs:
                quantity = order_obj.quantity
                revenue_quantity['inventoryId'] = inventory_obj.id
                revenue_quantity['quantity'] = quantity

        Response['status'] = 200
        Response['revenue_quantity'] = revenue_quantity
        return Response

class TopTrendingProducts(APIView):
    def post(self,request):
        data = request.data
        vendorId = data['vendorId']
        inventory_objs = Inventory.objects.filter(vendor=vendorId)
        Response = {}
        trending = []
        for inventory_obj in inventory_objs:
            order_inventory_objs = Order.objects.filter(inventory=inventory_obj.id,time__range=(datetime.datetime.now()-datetime.timedelta(days=14),datetime.datetime.now()-datetime.timedelta(days=7)))
            product_quantity = []
            for order_inventory_obj in order_inventory_objs:
                quantity = order_obj.quantity
                net_revenue =  net_revenue + product_obj.selling_price*quantity
                product_quantity.append(product_obj.id)
            order_inventory_objs = Order.objects.filter(inventory=inventory_obj.id,time__range=(datetime.datetime.now()-datetime.timedelta(days=7),datetime.datetime.now()-datetime.timedelta(days=0)))
            for order_inventory_obj in order_inventory_objs:
                quantity = order_obj.quantity
                net_revenue =  net_revenue + product_obj.selling_price*quantity
                if product_obj.id in product_quantity:
                    trending.append(product_obj.id)
        Response['status'] = 200
        Response['trening'] = trending