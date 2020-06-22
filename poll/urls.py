
from django.urls import path
from poll.views import index,details,poll,PollView

urlpatterns = [
    path('add/',PollView.as_view(),name='poll_add'),
    path('<int:id>/edit/',PollView.as_view(),name='poll_edit'),
    path('<int:id>/delete/',PollView.as_view(),name='poll_delete'),

    path('',index, name='polls_list'),
    path('<int:id>/details/',details,name='polls_detail'),
    path('<int:id>/',poll,name='single_poll'),


]