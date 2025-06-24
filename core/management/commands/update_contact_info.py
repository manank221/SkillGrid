from django.core.management.base import BaseCommand
from core.models import SiteSettings


class Command(BaseCommand):
    help = 'Updates contact information in the database'

    def handle(self, *args, **options):
        try:
            settings = SiteSettings.objects.first()
            if settings:
                settings.contact_email = 'skillgrit3@gmail.com'
                settings.contact_phone = '+918604807356'
                settings.save()
                self.stdout.write(
                    self.style.SUCCESS('Successfully updated contact information.')
                )
                self.stdout.write(f'Email: {settings.contact_email}')
                self.stdout.write(f'Phone: {settings.contact_phone}')
            else:
                self.stdout.write(
                    self.style.ERROR('No site settings found. Please run setup_initial_data first.')
                )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error updating contact information: {e}')
            ) 