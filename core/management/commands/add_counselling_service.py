from django.core.management.base import BaseCommand
from core.models import Service

class Command(BaseCommand):
    help = 'Adds a new Counselling service to the database'

    def handle(self, *args, **options):
        self.stdout.write('Checking for Counselling service...')

        service_data = {
            "title": "Counselling",
            "category": "consulting",
            "description": "Providing professional guidance and support to help you navigate personal or professional challenges.",
            "detailed_description": "Our counselling services offer a confidential and supportive environment to address a wide range of issues. Whether you're seeking guidance on career development, personal growth, or specific life challenges, our experienced counselors are here to help you find clarity and develop effective strategies. We believe in a client-centered approach, tailoring each session to your unique needs and goals.",
            "features": [
                "One-on-one confidential sessions",
                "Career and personal development",
                "Goal setting and strategy",
                "Supportive and non-judgmental environment"
            ],
            "icon_class": "fas fa-hands-helping",
            "order": 60
        }

        obj, created = Service.objects.update_or_create(
            title=service_data['title'],
            defaults=service_data
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Successfully added the "Counselling" service.'))
        else:
            self.stdout.write(self.style.WARNING('The "Counselling" service already exists. Content has been updated.')) 