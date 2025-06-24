from django.core.management.base import BaseCommand
from core.models import SiteSettings

class Command(BaseCommand):
    help = 'Updates the site contact email if it exists.'

    def handle(self, *args, **options):
        try:
            settings = SiteSettings.objects.first()
            if settings:
                settings.contact_email = 'skillgrit3@gmail.com'
                settings.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully updated contact email to {settings.contact_email}'))
            else:
                self.stdout.write(self.style.WARNING('No site settings found. Please run setup_initial_data first.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}')) 