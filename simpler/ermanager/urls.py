from django.conf.urls import patterns, include, url
from ermanager import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simpler.views.home', name='home'),
    # url(r'^simpler/', include('simpler.urls')),

    url(r'^bigscreen/$', views.big_board, name='big_screen'),

    url(r'^waitingscreen/$', views.waiting_board, name='waiting_screen'),

    url(r'^doctor_page/$',views.doctor_page, name='doctor_page'),

    #url(r'^nurse_page/$', views.nurse_page, name='nurse_page'),

    #url(r'^patient_nurse_mod/(?P<patient_id>\d+)/$',views.patient_nurse_mod,name='patient_nurse_mod'),

    #url(r'^patient/(?P<patient_id>\d+)/$',views.patient_nurse_edit,name='patient_nurse_edit'),

    url(r'^patient/(?P<patient_id>\d+)/$',views.patient_edit,name='patient_edit'),

    url(r'^patient_mod/(?P<patient_id>\d+)/$',views.patient_mod,name='patient_mod'),

    url(r'^submit_edit/$',views.submit_edit, name='submit_patient'),
    url(r'^patient_report/(?P<patient_id>\d+)/$',views.patient_report,name='patient_report'),

    )
