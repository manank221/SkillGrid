import datetime
from django.core.management.base import BaseCommand
from news.models import NewsArticle

class Command(BaseCommand):
    help = 'Adds or updates news articles from GKToday for Science & Technology'

    def handle(self, *args, **options):
        self.stdout.write('Starting to add or update news articles...')

        news_items = [
            {
                "title": "EMM-Negative Blood Group System",
                "date": "2025-06-24",
                "content": "The International Society of Blood Transfusion (ISBT) has officially recognized a new blood group system named EMM-negative, also known as Gwada negative. This rare blood type is characterized by the absence of EMM antigens on red blood cells. The designation emerged from the unique case of an individual in Guadeloupe whose blood showed unusual properties, leading to this significant hematological discovery. This finding expands our understanding of human blood diversity and has important implications for transfusion medicine and genetic research."
            },
            {
                "title": "Newborn Screening for Sickle Cell Disease in India",
                "date": "2025-06-23",
                "content": "In recent years, India has made significant strides in addressing sickle cell disease (SCD) through nationwide newborn screening initiatives. A comprehensive study conducted by the Indian Council of Medical Research (ICMR) highlighted the effectiveness of early detection in managing the disease and reducing mortality. The program aims to screen all newborns in high-prevalence areas, allowing for timely intervention, genetic counseling for families, and better long-term health outcomes for affected children. This proactive approach is a critical step in tackling the burden of SCD in the country."
            },
            {
                "title": "Snowflake Yeast Reveals Into Multicellularity",
                "date": "2025-06-23",
                "content": "Recent studies on 'snowflake yeast' have revealed intriguing vital information about the evolutionary leap from single-celled to multicellular organisms. This unique yeast, which forms branching, snowflake-like colonies, has become a focal point for scientists studying the origins of complex life. Researchers have observed how these simple organisms evolve to develop specialized cells and cooperative behaviors, providing a living model for the processes that may have led to the first animals on Earth billions of years ago."
            },
            {
                "title": "Covid-19 Variant NB.1.8.1",
                "date": "2025-06-21",
                "content": "The global landscape of the Covid-19 pandemic continues to evolve with the identification of new variants. The recent emergence of the NB.1.8.1 variant, nicknamed 'Nimbus', has drawn the attention of health officials due to its rapid transmission rates in several regions. Scientists are currently studying its genetic makeup to understand its potential impact on vaccine efficacy and disease severity. Continuous surveillance and genomic sequencing remain crucial tools in monitoring the virus's evolution and informing public health responses."
            },
            {
                "title": "WHO Guidelines for Sickle Cell Disease Management",
                "date": "2025-06-20",
                "content": "The World Health Organization (WHO) has introduced its first-ever global guideline for managing sickle cell disease (SCD) specifically during pregnancy. This landmark initiative addresses a critical health challenge that impacts both mothers and their unborn children, particularly in regions with a high prevalence of the disease. The guidelines provide evidence-based recommendations for healthcare providers on screening, management of complications, and ensuring safe pregnancies and deliveries, aiming to reduce maternal and infant mortality associated with SCD."
            },
            {
                "title": "Voyager 1 Discovers Superheated Plasma Beyond Pluto",
                "date": "2025-06-19",
                "content": "NASA's Voyager 1 spacecraft made discovery in the realm of space exploration. From nearly 24 billion kilometres away, it detected a shell of superheated plasma at the heliopause,..."
            },
            {
                "title": "Novel Nanoparticle Synthesis Method for Cancer Therapy",
                "date": "2025-06-18",
                "content": "Recent advancements in cancer treatment have brought into light a new one-step colloidal synthesis method for nanoparticles. This innovative approach focuses on creating nanoparticles with a unique shell..."
            },
            {
                "title": "Advanced Proton Therapy for Cancer Treatment",
                "date": "2025-06-17",
                "content": "Recently, a team of experts in the United States achieved a breakthrough in cancer treatment. They successfully employed step-and-shoot spot-scanning proton arc therapy, known as SPArc, to treat..."
            },
            {
                "title": "Air India Crash Victim Identification Methods",
                "date": "2025-06-16",
                "content": "In the wake of the tragic Air India Boeing 787 Dreamliner crash in Ahmedabad, authorities have turned to DNA analysis to identify the victims. This process is crucial..."
            },
            {
                "title": "New Jumping Spider Species",
                "date": "2025-06-16",
                "content": "Recent research has revealed a new species of jumping spider in southern India. This species belongs to the Spartaeinae subfamily. It is as it marks the first discovery..."
            }
        ]

        updated_count = 0
        created_count = 0

        for item in news_items:
            publication_date = datetime.datetime.strptime(item['date'], '%Y-%m-%d').date()
            
            obj, created = NewsArticle.objects.update_or_create(
                title=item['title'],
                defaults={
                    'content': item['content'],
                    'category': 'tech',
                    'publication_date': publication_date
                }
            )

            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Successfully added article: "{item["title"]}"'))
            else:
                updated_count += 1
                self.stdout.write(self.style.WARNING(f'Successfully updated article: "{item["title"]}"'))

        self.stdout.write(self.style.SUCCESS(f'Finished processing. Created: {created_count}, Updated: {updated_count}')) 