from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Service, Testimonial, About, SiteSettings
from portfolio.models import Project
from news.models import NewsArticle


class Command(BaseCommand):
    help = 'Set up initial data for the freelance website'

    def handle(self, *args, **options):
        self.stdout.write('Setting up initial data...')
        
        # Create superuser if none exists
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Superuser created: admin/admin123'))
        
        # Create site settings
        if not SiteSettings.objects.exists():
            SiteSettings.objects.create(
                site_name="My Portfolio",
                site_description="Professional freelance services for all your creative and digital needs.",
                hero_title="Professional Freelance Services",
                hero_subtitle="Transforming ideas into exceptional digital experiences",
                hero_description="Specializing in web design, content writing, graphic design, logo creation, poster design, and translation services. Let's bring your vision to life!",
                contact_email="skillgrit3@gmail.com",
                contact_phone="+918604807356",
                address="Available Worldwide",
                social_linkedin="https://linkedin.com/in/yourprofile",
                social_twitter="https://twitter.com/yourprofile",
                social_instagram="https://instagram.com/yourprofile",
                social_behance="https://behance.net/yourprofile"
            )
            self.stdout.write(self.style.SUCCESS('Created default site settings.'))
        
        # Create services
        if not Service.objects.exists():
            services_data = [
                {
                    'title': 'Web Design',
                    'description': 'Modern, responsive websites that engage your audience and drive results. From landing pages to full e-commerce solutions.',
                    'category': 'web',
                    'icon_class': 'fas fa-laptop-code',
                    'features': ['Responsive Design', 'UI/UX Optimization', 'SEO-Friendly', 'Fast Loading'],
                    'order': 1
                },
                {
                    'title': 'Content Writing',
                    'description': 'Compelling, SEO-optimized content that tells your story and connects with your audience.',
                    'category': 'content',
                    'icon_class': 'fas fa-pen-fancy',
                    'features': ['Blog Posts & Articles', 'Website Copy', 'Marketing Materials', 'SEO Optimization'],
                    'order': 2
                },
                {
                    'title': 'Graphic Design',
                    'description': 'Eye-catching visuals that strengthen your brand identity and communicate your message effectively.',
                    'category': 'graphic',
                    'icon_class': 'fas fa-palette',
                    'features': ['Brand Identity', 'Social Media Graphics', 'Print Materials', 'Digital Assets'],
                    'order': 3
                },
                {
                    'title': 'Logo & Poster Design',
                    'description': 'Memorable logos and impactful posters that make your brand stand out from the competition.',
                    'category': 'logo',
                    'icon_class': 'fas fa-paint-brush',
                    'features': ['Logo Design', 'Poster Creation', 'Brand Guidelines', 'Vector Formats'],
                    'order': 4
                },
                {
                    'title': 'Translation Services',
                    'description': 'Accurate and culturally appropriate translations that help you reach global audiences.',
                    'category': 'translation',
                    'icon_class': 'fas fa-language',
                    'features': ['Document Translation', 'Website Localization', 'Marketing Materials', 'Cultural Adaptation'],
                    'order': 5
                },
                {
                    'title': 'Digital Marketing',
                    'description': 'Strategic digital marketing solutions to boost your online presence and drive growth.',
                    'category': 'marketing',
                    'icon_class': 'fas fa-mobile-alt',
                    'features': ['Social Media Management', 'Email Marketing', 'Content Strategy', 'Analytics & Reporting'],
                    'order': 6
                }
            ]
            
            for service_data in services_data:
                Service.objects.create(**service_data)
            
            self.stdout.write(self.style.SUCCESS('Services created'))
        
        # Create testimonials
        if not Testimonial.objects.exists():
            testimonials_data = [
                {
                    'client_name': 'Sarah Johnson',
                    'client_position': 'CEO',
                    'client_company': 'TechStart Inc.',
                    'content': 'Exceptional web design work! The website exceeded our expectations and helped increase our online conversions significantly.',
                    'rating': 5,
                    'order': 1
                },
                {
                    'client_name': 'Michael Chen',
                    'client_position': 'Founder',
                    'client_company': 'GreenEats',
                    'content': 'Professional, creative, and reliable. The logo design perfectly captured our brand essence and we couldn\'t be happier!',
                    'rating': 5,
                    'order': 2
                },
                {
                    'client_name': 'Emily Rodriguez',
                    'client_position': 'Marketing Director',
                    'client_company': 'HealthPlus',
                    'content': 'Outstanding content writing services. The blog posts are engaging, SEO-optimized, and have helped boost our organic traffic.',
                    'rating': 5,
                    'order': 3
                }
            ]
            
            for testimonial_data in testimonials_data:
                Testimonial.objects.create(**testimonial_data)
            
            self.stdout.write(self.style.SUCCESS('Testimonials created'))
        
        # Create about section
        if not About.objects.exists():
            About.objects.create(
                title='About Us',
                subtitle='Passionate freelance professional with expertise in multiple creative and digital disciplines',
                content='I\'m a passionate freelance professional with expertise in multiple creative and digital disciplines. With years of experience in web design, content creation, graphic design, and translation services, I help businesses and individuals bring their visions to life.\n\nMy approach combines creativity with strategic thinking, ensuring that every project not only looks great but also achieves your business goals. I believe in building long-term relationships with clients based on trust, quality, and results.',
                skills=['HTML/CSS', 'JavaScript', 'React', 'WordPress', 'Adobe Creative Suite', 'Figma', 'SEO', 'Content Strategy', 'Translation', 'UI/UX Design'],
                experience_years=5,
                projects_completed=50,
                happy_clients=30,
                satisfaction_rate=100
            )
            self.stdout.write(self.style.SUCCESS('About section created'))
        
        # Create sample projects
        if not Project.objects.exists():
            projects_data = [
                {
                    'title': 'E-commerce Website',
                    'description': 'Modern responsive design with shopping cart functionality for an online retail store.',
                    'category': 'web',
                    'client': 'TechStart Inc.',
                    'technologies_used': ['HTML5', 'CSS3', 'JavaScript', 'React', 'Node.js'],
                    'is_featured': True,
                    'order': 1
                },
                {
                    'title': 'Brand Identity Package',
                    'description': 'Complete brand identity including logo, colors, and guidelines for a startup company.',
                    'category': 'graphic',
                    'client': 'GreenEats',
                    'technologies_used': ['Adobe Illustrator', 'Photoshop', 'InDesign'],
                    'is_featured': True,
                    'order': 2
                },
                {
                    'title': 'Tech Startup Logo',
                    'description': 'Minimalist logo design for innovative tech company with modern aesthetic.',
                    'category': 'logo',
                    'client': 'InnovateTech',
                    'technologies_used': ['Adobe Illustrator', 'Vector Graphics'],
                    'is_featured': True,
                    'order': 3
                },
                {
                    'title': 'Blog Content Series',
                    'description': 'SEO-optimized blog posts for health and wellness brand with engaging content.',
                    'category': 'content',
                    'client': 'HealthPlus',
                    'technologies_used': ['Content Strategy', 'SEO', 'WordPress'],
                    'is_featured': False,
                    'order': 4
                },
                {
                    'title': 'Landing Page Design',
                    'description': 'High-converting landing page for SaaS product with modern design.',
                    'category': 'web',
                    'client': 'SaaSPro',
                    'technologies_used': ['HTML5', 'CSS3', 'JavaScript', 'Bootstrap'],
                    'is_featured': False,
                    'order': 5
                },
                {
                    'title': 'Social Media Campaign',
                    'description': 'Complete social media graphics package for restaurant with consistent branding.',
                    'category': 'graphic',
                    'client': 'TasteBuds',
                    'technologies_used': ['Adobe Photoshop', 'Canva', 'Social Media Design'],
                    'is_featured': False,
                    'order': 6
                }
            ]
            
            for project_data in projects_data:
                Project.objects.create(**project_data)
            
            self.stdout.write(self.style.SUCCESS('Sample projects created'))
        
        # Delete existing news articles before creating new ones
        if NewsArticle.objects.exists():
            NewsArticle.objects.all().delete()
            self.stdout.write(self.style.WARNING('Removed existing news articles.'))

        # Create news articles
        news_data = [
            # International
            {
                'title': 'Global Leaders Convene for Climate Action Summit',
                'content': 'Top international leaders met this week to forge a new path on climate change. The summit focused on collaborative solutions, including new commitments to reduce greenhouse gas emissions and investment in green technologies. A major outcome was the establishment of a global fund to support developing nations in their transition to sustainable energy sources.',
                'category': 'international',
                'image': 'https://media.istockphoto.com/id/1368853185/photo/group-of-diverse-business-people-on-panel-discussion.jpg?s=612x612&w=0&k=20&c=Jv_n5w6vYyD-A2LcX3h24qQy_hGkR1K-m8hYvhtrD4E=',
            },
            {
                'title': 'Economic Forum Highlights Digital Transformation',
                'content': 'The annual economic forum emphasized the rapid pace of digital transformation and its profound impact on global markets. Experts discussed the future of work, the ethics of artificial intelligence, and the critical importance of investing in new technologies to stay competitive. Breakout sessions covered topics from blockchain integration to the rise of the metaverse.',
                'category': 'international',
                'image': 'https://media.istockphoto.com/id/1399432454/photo/international-technology-conference-male-host-asking-caucasian-female-ceo-a-question-in.jpg?s=612x612&w=0&k=20&c=L_qT4L4vT9tA5V6eK3q-Qh88SgZJ2b5z1T5yL1w1Q4Q=',
            },
            # National
            {
                'title': 'New Infrastructure Bill Passed by Parliament',
                'content': 'A comprehensive infrastructure bill was passed today after months of debate. The bill allocates billions for the modernization of the nation\'s roads, bridges, public transport systems, and broadband networks. Proponents argue the project will create thousands of jobs over the next decade and stimulate economic growth.',
                'category': 'national',
                'image': 'https://media.istockphoto.com/id/1291244439/photo/construction-in-progress-of-a-mass-rapid-transit-line.jpg?s=612x612&w=0&k=20&c=7djdP_M5hVj_lC0sC-s-Cq3Q9a1d_kC7s-lJ1P2tK-4=',
            },
            {
                'title': 'Urban Renewal Project Transforms City Center',
                'content': 'A multi-year urban renewal project is revitalizing the city center, with new parks, residential buildings, and commercial spaces. The project aims to create a more walkable and sustainable downtown area, attracting new businesses and residents while preserving historical landmarks.',
                'category': 'national',
                'image': 'https://media.istockphoto.com/id/1492257913/photo/modern-wealthy-apartment-complex-with-eco-friendly-features-in-santa-clara-cupertino-in.jpg?s=612x612&w=0&k=20&c=fG5K1u0xK0xL-oPS1lXbO13_Hk6w9rEaR_Gz-83vS2o=',
            },
            # Tech
            {
                'title': 'Breakthrough in Healthcare: A New Era of Medicine',
                'content': 'Scientists have announced a major breakthrough in medical research that could revolutionize how we treat a range of diseases. This new discovery opens the door for personalized medicine, offering hope for more effective treatments with fewer side effects. Clinical trials are expected to begin next year.',
                'category': 'tech',
                'image': 'https://media.istockphoto.com/id/1318617359/photo/female-scientist-looking-under-microscope-and-using-laptop-in-a-laboratory.jpg?s=612x612&w=0&k=20&c=fG7x5Uq-hW23v21Wq7Pq3-p_sP4M4C4lB-q8V9dZ_J4=',
            },
            {
                'title': 'The Future of AI in Modern Art',
                'content': 'Artificial intelligence is no longer just for data. A new wave of AI-powered tools is allowing artists to explore new frontiers of creativity. From generating stunning visual art to composing complex musical pieces, AI is becoming a powerful collaborator in the art world, raising new questions about the nature of creativity itself.',
                'category': 'tech',
                'image': 'https://images.unsplash.com/photo-1655720224164-9f79513a051c?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            },
            # Sports
            {
                'title': 'Championship Finals: A Historic Victory',
                'content': 'The national soccer team clinched a historic victory in the championship finals after a dramatic penalty shootout. The team\'s goalkeeper made a stunning final save, securing the cup for the first time in two decades. Celebrations erupted across the country as fans took to the streets to honor their heroes.',
                'category': 'sports',
                'image': 'https://media.istockphoto.com/id/876899218/photo/celebrating-the-victory-after-soccer-match.jpg?s=612x612&w=0&k=20&c=a4eLPiY7u5BwA0y4206rowV6Lg7sHhYm32oA7xJmPS0=',
            },
            {
                'title': 'Grand Slam Glory: Tennis Star\'s Historic Win',
                'content': 'A rising tennis star has made history by winning her first Grand Slam title after a grueling three-set final. Her powerful serves and relentless baseline game proved too much for the world number one. The victory marks a new era in women\'s tennis and crowns a new queen of the court.',
                'category': 'sports',
                'image': 'https://media.istockphoto.com/id/1218137683/photo/female-tennis-player-celebrating-victory-during-match-on-clay-court.jpg?s=612x612&w=0&k=20&c=pSJB7pLwVAPJv4tA7s7erH9oCS83yX_w9YEo2ZkHl_8=',
            },
        ]

        for article_data in news_data:
            NewsArticle.objects.create(**article_data)
        
        self.stdout.write(self.style.SUCCESS('Created news articles with real images'))

        self.stdout.write(self.style.SUCCESS('Initial data setup complete.'))