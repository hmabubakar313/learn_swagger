from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path, re_path, include
# drf_yasg code starts here
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Django API",
        default_version='v1',
        description="Welcome to the world of Django API",
        terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="jason@jaseci.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #<-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  #<-- Here
    path('student_list/',views.student_list,name='student_list'),
    path('create_student/',views.create_student,name='create_student'),
    path('update_student/<int:pk>/',views.update_student,name='update_student'),
    path('delete_student/<int:pk>/',views.delete_student,name='delete_student')
] 



