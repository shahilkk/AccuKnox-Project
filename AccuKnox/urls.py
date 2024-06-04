
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.schemas import get_schema_view

from rest_framework_simplejwt import views as jwt_views 



API_Title           = 'AccuKnox APIs'

schema_view         = get_schema_view(title=API_Title)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('User.urls')),
    path('api/v1/section/',include('Posts.urls')),
    path('auth/', include('djoser.urls')),
    path('token/', jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'), 
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),name ='token_refresh'), 
]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static('/static/build/', document_root=os.path.join(BASE_DIR, 'react','build', 'static'))
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)