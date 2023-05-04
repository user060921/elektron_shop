from .models import Category


def menu_category_list(request):
    category = Category.objects.all()
    return dict(category=category)


