from django.contrib import admin

from swaps.images.models import OfferImage


class OfferImageAdminInline(admin.TabularInline):
  model = OfferImage
  extra = 0
