from django.db import models


class VariationCategoryChoices(models.TextChoices):
    COLOR = "color", "Color"
    SIZE = "size", "Size"


class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(
            variation_category=VariationCategoryChoices.COLOR,
            is_active=True
        )

    def sizes(self):
        return super(VariationManager, self).filter(
            variation_category=VariationCategoryChoices.SIZE,
            is_active=True
        )
