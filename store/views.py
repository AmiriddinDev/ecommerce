from itertools import product
from lib2to3.fixes.fix_input import context

from django.views.generic import DetailView, ListView

from .models.products import Product
from .models.variations import Variation, VariationCategoryChoices

# Create your views here.

class StoreViews(ListView):
    model = Product
    template_name = "store/list.html"
    context_object_name = "products"
    queryset = Product.objects.filter(is_available=True)

store_list_view = StoreViews.as_view()

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/detail.html'
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['size_variants'] = Variation.objects.filter(
            product=product, variation_category=VariationCategoryChoices.SIZE
        )
        context['color_variants'] = Variation.objects.filter(
            product=product, variation_category=VariationCategoryChoices.COLOR
        )
        return context



product_detail_view = ProductDetailView.as_view()