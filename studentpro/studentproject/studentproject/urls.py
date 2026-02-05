from django.contrib import admin
from django.urls import path
from students import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('superadmin/', views.superuser_login, name='superuser_login'),
    path('admin/', admin.site.urls),

    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
