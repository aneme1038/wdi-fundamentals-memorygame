#created this file to create the paths for linking templates
#need this line to get Path
from django.urls import path
#import from ALL the VIEWS
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    #passing in the question_id from views for detail
    path('<int:question_id>/', views.detail, name='detail'),
    #passing question_id again for the results view
    path('<int:question_id>/results/', views.results, name='results'),
    #pass in vote
    path('<int:question_id>/vote/', views.vote, name='vote')
]
