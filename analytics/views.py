from django.shortcuts import render
from django.db.models import Sum
import datetime
import json
from pytz import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from analytics.models import *

# Create your views here.
class FetchVendorInventoryStores(APIView):

    def post(self, request):
        response = {"status":500}
        try:
            data = request.data
            vendor_id = data.get("vendor_id")
            store_count = Inventory.objects.filter(vendor__id=vendor_id).count()
            response["store_count"] = store_count
            response["status"] = 200
        except Exception as ex:
            raise ex
        return Response(data=response)


class FetchVendorUniqueProducts(APIView):

    def post(self, request):
        response = {"status":500}
        try:
            data = request.data
            vendor_id = data.get("vendor_id")
            inventory_stores = Inventory.objects.filter(vendor__id=vendor_id)
            product_count = Product.objects.filter(inventory__in=inventory_stores).distinct.count()
            response["product_count"] = product_count
            response["status"] = 200
        except Exception as ex:
            raise ex
        return Response(data=response)


class FetchMonthlyVendorRevenue(APIView):

    def post(self, request):
        response = {"status":500}
        try:
            data = request.data
            vendor_id = data.get("vendor_id")
            orders = Order.objects.filter(inventory__vendor__id=vendor_id, time__gte = datetime.now() - datetime.timedelta(days=30))
            monthly_revenue = 0
            for order in orders:
                monthly_revenue += Product.objects.get(id=order.product) * order.quantity    
            response["monthly_revenue"] = monthly_revenue
            response["status"] = 200
        except Exception as ex:
            raise ex
        return Response(data=response)


class FetchMonthlyVendorOrdersRevenue(APIView):

    def post(self, request):
        response = {"status":500}
        try:
            data = request.data
            vendor_id = data.get("vendor_id")
            order_count = Order.objects.filter(inventory__vendor__id=vendor_id, time__gte = datetime.now() - datetime.timedelta(days=30)).count()    
            response["order_count"] = order_count
            response["status"] = 200
        except Exception as ex:
            raise ex
        return Response(data=response)


class FetchVendorStoreList(APIView):

    def post(self, request):
        response = {"status":500}
        try:
            data = request.data
            store_list = []
            vendor_id = data.get("vendor_id")
            inventory_stores = Inventory.objects.filter(vendor__id=vendor_id).values_list('id', flat=True)
            for store in inventory_stores:
                products = InventoryProduct.objects.filter(inventory__id=store)
                products_list = []
                for product in products:
                    temp_dict = {}
                    temp_dict['product_name'] = Product.objects.get(id=product.id).name
                    temp_dict['quantity'] = product.quantity
                    products_list.append(temp_dict)
                temp_dict = {}
                temp_dict['store'] = store
                temp_dict['products'] = products_list
                store_list.append(temp_dict)    
            response["store_list"] = store_list
            response["status"] = 200
        except Exception as ex:
            raise ex
        return Response(data=response)


class FetchStoreStrengthList(APIView):

    def post(self, request):
        response = {"status":500}
        try:
            data = request.data
            store_strength = []
            vendor_id = data.get("vendor_id")
            product_id = data.get("product_id")
            inventory_stores = Inventory.objects.filter(vendor__id=vendor_id)
            total_product_quantity = InventoryProduct.objects.filter(inventory__in=inventory_stores, product__id=product_id).aggregate(Sum('quantity'))
            for store in inventory_stores:
                product_quantity = InventoryProduct.objects.get(inventory__id=store.id, product__id=product_id).quantity
                temp_dict = {}
                temp_dict['store'] = store.id
                temp_dict['product_strength'] = (product_quantity*100)/float(total_product_quantity)
                store_strength.append(temp_dict)    
            response["store_strength"] = store_strength
            response["status"] = 200
        except Exception as ex:
            raise ex
        return Response(data=response)


class FetchTrendingVendorRegion(APIView):

    def post(self, request):
        response = {"status":500}
        try:
            data = request.data
            store_strength = []
            vendor_id = data.get("vendor_id")
            inventory_stores = Inventory.objects.filter(vendor__id=vendor_id)
            region_sell_count = {}
            for store in inventory_stores:
                region_sell_count[store.region.id] += Order.objects.filter(inventory__id=store.id).count()
            response["trending_region"] = max(region_sell_count, key=region_sell_count.get)
            response["status"] = 200
        except Exception as ex:
            raise ex
        return Response(data=response)


