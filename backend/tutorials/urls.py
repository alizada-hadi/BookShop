from django.urls import path
from . import views

urlpatterns = [
    path("api/", views.TutorialListView.as_view(), name="list"),
    path("api/tutorial/<int:pk>/",
         views.TutorialDetailView.as_view(), name="detail"),
    path("api/tutorial/<int:pk>/update/",
         views.TutorialUpdateView.as_view(), name="update"),
    path("api/tutorial/<int:pk>/delete/",
         views.TutorialDeleteView.as_view(), name="delete"),
    path("api/create/", views.TutorialCreateView.as_view(), name="create"),
]
