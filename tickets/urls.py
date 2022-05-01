from rest_framework.routers import SimpleRouter
from tickets.views import TicketViewSet

router = SimpleRouter()
router.register('', TicketViewSet, basename='tickets')

urlpatterns = router.urls
