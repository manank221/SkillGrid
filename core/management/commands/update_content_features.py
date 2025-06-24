from django.core.management.base import BaseCommand
from core.models import Service

class Command(BaseCommand):
    help = 'Update features for Content Writing service with emoji icons and bold keywords.'

    def handle(self, *args, **options):
        try:
            s = Service.objects.get(title='Content Writing')
            s.features = [
                '📝 <strong>Blog Posts & Articles</strong>',
                '📄 <strong>Website Copy</strong>',
                '🎯 <strong>Marketing Materials</strong>',
                '🔍 <strong>SEO Optimization</strong>'
            ]
            s.save()
            self.stdout.write(self.style.SUCCESS('Features for Content Writing updated successfully!'))
        except Service.DoesNotExist:
            self.stdout.write(self.style.ERROR('Content Writing service not found.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Unexpected error: {e}')) 