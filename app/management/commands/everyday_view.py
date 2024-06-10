from app.models import todays_view, views, PcNames
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    def handle(self, *args, **options):

        PcNames_obj = PcNames.objects.create(name='local')
        sq_obj = todays_view.objects.all()
        
        for i in sq_obj :
            aws_obj, created = views.objects.using('aws').get_or_create(date=i.date,PcNames=PcNames_obj)
            aws_obj.PcNames = PcNames_obj.name
            aws_obj.views = i.views
            aws_obj.save()