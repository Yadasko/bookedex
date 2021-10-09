from django.contrib import admin
from .models import Book
from .models import Author
from .models import BookHunter
from .models import CollectedBook
from .models import WantedBook


# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookHunter)
admin.site.register(CollectedBook)
admin.site.register(WantedBook)
