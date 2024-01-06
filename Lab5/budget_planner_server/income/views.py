from rest_framework import viewsets
from .models import Income
from .serializers import IncomeSerializer
import logging

logger = logging.getLogger(__name__)

class IncomeViewSet(viewsets.ModelViewSet):
    logger.info('Handling request for Income view.')
    try:
        queryset = Income.objects.all()
        serializer_class = IncomeSerializer
    except Exception as e:
        logger.error(f'Error in Income view: {e}')
    logger.info('Finished handling request for Income view')
