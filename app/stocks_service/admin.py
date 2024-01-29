from django.contrib import admin

from .models import (
    Stock,
    Portfolio,
    Recommendation,
    UserProfile,
)


admin.site.register(Stock)
admin.site.register(Portfolio)
admin.site.register(Recommendation)
admin.site.register(UserProfile)
