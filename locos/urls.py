from django.urls import path
from locos.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile1/', profile1, name='profile1'),
    path('profile2/', profile2, name='profile2'),
    path('profile3/', profile3, name='profile3'),
    path('profile4/', profile4, name='profile4'),
    path('celebre/', celebre, name='celebre'),
    path('british/', british, name='british'),
    path('brad/', brad, name='brad'),
    path('america/', america, name='america'),
    path('intretinere/', intretinere, name='intretinere'),
    path('proba/', proba, name='proba'),
    path('romania/', romania, name='romania'),
    path('scotsman/', flying_scotsman, name='scotsman')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
