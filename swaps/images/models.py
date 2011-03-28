from os.path import join

from django.db import models
from django.utils.translation import ugettext_lazy as _

from swaps.models import Offer

def offerimage_upload_to(instance, filename):
    return join('swaps', instance.pk, filename)

class OfferImage(models.Model):
  offer = models.ForeignKey(Offer, related_name="images")
  order = models.PositiveIntegerField(_('order'))
  image = models.ImageField(_('image'), upload_to=offerimage_upload_to)
