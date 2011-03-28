from django.contrib import admin
from django.conf import settings
from swaps.models import Offer, Swap


offer_inlines = []

if 'swaps.images' in settings.INSTALLED_APPS:
  from swaps.images.admin import OfferImageAdminInline
  offer_inlines += [OfferImageAdminInline,]

class OfferAdmin(admin.ModelAdmin):
    list_display        = ('offerer', 'short_description', 'offering', 'want', 'state', 'swapped_by')
    list_filter         = ('offerer', 'state')
    search_fields       = ('short_description', 'offering', 'want')
    inlines = offer_inlines

admin.site.register(Offer, OfferAdmin)

class SwapAdmin(admin.ModelAdmin):
    list_display        = ('proposing_offer', 'responding_offer', 'state', 'conflicted_by')
    list_filter         = ('state',)

admin.site.register(Swap, SwapAdmin)
