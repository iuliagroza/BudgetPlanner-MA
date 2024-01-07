from rest_framework import viewsets
from .models import Income
from .serializers import IncomeSerializer
import logging

logger = logging.getLogger(__name__)

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    def list(self, request, *args, **kwargs):
        logger.info('Handling request for Income list view.')
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            logger.error(f'Error in Income list view: {e}')
            raise
        finally:
            logger.info('Finished handling request for Income list view')
