from django.core.management.base import BaseCommand
from core.models import Service

class Command(BaseCommand):
    help = 'Fix features for Content Writing to be a list of strings.'

    def handle(self, *args, **options):
        try:
            s = Service.objects.get(title='Content Writing')
            s.features = [
                "📝 Blog Posts & Articles",
                "📄 Website Copy",
                "🎯 Marketing Materials",
                "🔍 SEO Optimization"
            ]
            s.save()
            self.stdout.write(self.style.SUCCESS('Features for Content Writing fixed to list of strings!'))
        except Service.DoesNotExist:
            self.stdout.write(self.style.ERROR('Content Writing service not found.')) 