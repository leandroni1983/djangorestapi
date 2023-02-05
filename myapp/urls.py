from rest_framework import routers
from .api.api import MyModelViesSet
router = routers.DefaultRouter()

router.register('api/projects', MyModelViesSet, 'projects')

urlpatterns = router.urls
