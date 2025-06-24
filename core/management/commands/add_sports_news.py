import datetime
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from news.models import NewsArticle

class Command(BaseCommand):
    help = 'Adds or updates sports news articles from India Today'

    def handle(self, *args, **options):
        self.stdout.write('Starting to add or update sports news articles...')

        news_items = [
            {
                "title": "Day 5 Live: Lunch called, England dominate morning session",
                "date": "2025-06-24",
                "content": "England (ENG) vs India (IND), 1st Test Day 5 Live Score and Updates: Ben Duckett and Zak Crawley have done exceedingly well to keep England ahead in the 1st Test match. 96 runs have been scored in the morning session of Day 5. India pacers have gone wicketless and are looking slightly toothless on the Leeds deck."
            },
            {
                "title": "ICC punishes Rishabh Pant for showing dissent at umpire's decision",
                "date": "2025-06-24",
                "content": "India's wicket-keeper-batter Rishabh Pant has been handed an official reprimand for breaching Level 1 of the ICC Code of Conduct during the Headingley Test for showing dissent at an umpire's decision."
            },
            {
                "title": "Emma Raducanu thanks Wimbledon for blocking stalker's ticket purchase",
                "date": "2025-06-24",
                "content": "Briton Emma Raducanu said she felt reassured about her safety after Wimbledon organisers prevented a man who had been stalking her from purchasing tickets for the Grand Slam, which begins on Monday."
            },
            {
                "title": "Neeraj Chopra targets Ostrava win ahead of Tokyo World Championships",
                "date": "2025-06-24",
                "content": "Ahead of his homecoming in Bengaluru with the Neeraj Chopra Classic on July 5, the Indian ace will look to make a mark at the Ostrava Golden Spike event as he enters as the favourite."
            },
            {
                "title": "Dilip Doshi dies: India, England players wear black armbands in Leeds tribute",
                "date": "2025-06-24",
                "content": "Former Indian spinner Dilip Doshi passed away on June 23 at age 77. India and England players observed a minute's silence while wearing black armbands in a tribute to the spinner on Tuesday, June 24."
            },
            {
                "title": "Rahul Dravid refused Rs 2.5 crore extra bonus for World Cup triumph",
                "date": "2025-06-23",
                "content": "As per reports, head coach Rahul Dravid graciously turned down an extra bonus of Rs 2.5 crore offered for India's T20 World Cup victory, stating his salary was sufficient."
            },
            {
                "title": "PM Modi shares 'asli story' of India's T20 World Cup win in Moscow",
                "date": "2025-06-23",
                "content": "Prime Minister Narendra Modi shared his experience of watching the thrilling T20 World Cup final while on a visit to Moscow, revealing the 'asli story' of India's victory from his perspective."
            }
        ]

        updated_count = 0
        created_count = 0

        for item in news_items:
            naive_date = datetime.datetime.strptime(item['date'], '%Y-%m-%d')
            aware_date = make_aware(naive_date)
            
            obj, created = NewsArticle.objects.update_or_create(
                title=item['title'],
                defaults={
                    'content': item['content'],
                    'category': 'sports',
                    'publication_date': aware_date
                }
            )

            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Successfully added article: "{item["title"]}"'))
            else:
                updated_count += 1
                self.stdout.write(self.style.WARNING(f'Successfully updated article: "{item["title"]}"'))

        self.stdout.write(self.style.SUCCESS(f'Finished processing. Created: {created_count}, Updated: {updated_count}')) 