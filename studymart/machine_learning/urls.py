from django.urls import path
from . import views

urlpatterns=[
path('ml/',views.machine_learning,name="machine_learning"),
path('knn/',views.knn,name="knn"),
path('decision_tree/',views.decision_tree,name="decision_tree"),
path('nearest_neighbour/',views.nearest_neighbour,name="nearest_neighbor"),
path('random_forest/',views.random_forest,name="random_forest")
# path('dl/',views.deep_learning),
# path('abt/',views.about_us),
]