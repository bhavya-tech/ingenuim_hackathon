from django.urls import path
from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from analytics.views import *
from django.conf import settings

urlpatterns = [
    path('fetch-vendor-inventory-stores/',FetchVendorInventoryStores.as_view()),
    path('fetch-vendor-unique-products/',FetchVendorUniqueProducts.as_view()),
    path('fetch-monthly-vendor-revenue/',FetchMonthlyVendorRevenue.as_view()),
    path('fetch-monthly-vendor-orders-revenue/',FetchMonthlyVendorOrdersRevenue.as_view()),
    path('fetch-vendor-store-list/',FetchVendorStoreList.as_view()),
    path('fetch-store-strength-list/',FetchStoreStrengthList.as_view()),
    path('fetch-trending-vendor-region/',FetchTrendingVendorRegion.as_view()),
    # *staticfiles_urlpatterns(),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
