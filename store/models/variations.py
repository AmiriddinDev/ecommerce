from django.db import models

from ..managers.variations import VariationManager, VariationCategoryChoices
from .products import BaseModel, Product


class Variation(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variations")
    variation_category = models.CharField(
        max_length=100, choices=VariationCategoryChoices.choices
    )
    variation_value = models.CharField(max_length=100)

    #Custom Managers
    objects = VariationManager()

    def __str__(self):
        return self.variation_value

    class Meta:
        verbose_name = "Variation"
        verbose_name_plural = "Variations"