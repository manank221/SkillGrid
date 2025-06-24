# Django Freelancing Website Setup Guide

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables
Copy `env_example.txt` to `.env` and configure:
```bash
cp env_example.txt .env
```

Edit `.env` with your settings:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 3. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Set Up Initial Data
```bash
python manage.py setup_initial_data
```

### 5. Create Static Files
```bash
python manage.py collectstatic
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see your website!

## 📁 Project Structure

```
freelance_website/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── env_example.txt          # Environment variables template
├── DJANGO_SETUP.md          # This file
├── 
├── freelance_website/        # Main Django project
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── 
├── core/                     # Core app (services, testimonials, about)
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py            # Service, Testimonial, About, SiteSettings models
│   ├── views.py             # Home, About, Services views
│   ├── admin.py             # Django admin configuration
│   ├── urls.py              # Core app URLs
│   └── management/          # Custom management commands
│       └── commands/
│           └── setup_initial_data.py
├── 
├── portfolio/                # Portfolio app
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py            # Project, ProjectImage models
│   ├── views.py             # Portfolio list and detail views
│   ├── admin.py             # Portfolio admin
│   └── urls.py              # Portfolio URLs
├── 
├── contact/                  # Contact app
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py            # ContactMessage model
│   ├── forms.py             # Contact form with validation
│   ├── views.py             # Contact form handling
│   ├── admin.py             # Contact admin
│   └── urls.py              # Contact URLs
├── 
├── templates/                # Django templates
│   ├── base.html            # Base template
│   ├── core/                # Core app templates
│   │   ├── home.html        # Home page
│   │   ├── about.html       # About page
│   │   └── services.html    # Services page
│   ├── portfolio/           # Portfolio templates
│   │   ├── portfolio_list.html
│   │   └── project_detail.html
│   └── contact/             # Contact templates
│       └── contact.html
├── 
├── static/                   # Static files (CSS, JS, images)
│   ├── css/
│   │   └── styles.css       # Main stylesheet
│   └── js/
│       └── script.js        # JavaScript functionality
└── 
└── media/                    # User-uploaded files (created automatically)
    └── portfolio/           # Portfolio images
```

## 🔧 Features

### ✅ Dynamic Content Management
- **Services**: Add, edit, and manage your freelance services
- **Portfolio**: Upload and organize your project work
- **Testimonials**: Manage client testimonials
- **About Section**: Update your professional information
- **Site Settings**: Configure contact info, social links, and site branding

### ✅ Admin Panel
Access at `/admin/` with credentials:
- Username: `admin`
- Password: `admin123`

### ✅ Contact Form
- Form validation
- Email notifications
- Message storage in database
- Admin interface for managing messages

### ✅ Portfolio Management
- Project categories
- Image uploads
- Project details and descriptions
- Featured projects

### ✅ Responsive Design
- Mobile-friendly
- Modern UI/UX
- Smooth animations
- SEO optimized

## 🛠️ Customization

### 1. Update Site Information
Go to Admin Panel → Site Settings and update:
- Site name and description
- Hero section content
- Contact information
- Social media links

### 2. Add Your Services
Admin Panel → Services:
- Add new services
- Set icons (FontAwesome classes)
- Add features list
- Set display order

### 3. Upload Portfolio Work
Admin Panel → Projects:
- Add project details
- Upload images
- Set categories
- Mark as featured

### 4. Add Testimonials
Admin Panel → Testimonials:
- Add client feedback
- Set ratings
- Organize by order

### 5. Update About Section
Admin Panel → About:
- Update your bio
- Add skills
- Set statistics

## 📧 Email Configuration

### Gmail Setup
1. Enable 2-factor authentication
2. Generate App Password
3. Update `.env` file:
```env
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Other Email Providers
Update `.env` with your provider's settings:
```env
EMAIL_HOST=smtp.yourprovider.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
```

## 🚀 Deployment

### Option 1: Heroku
1. Create Heroku account
2. Install Heroku CLI
3. Create `Procfile`:
```
web: gunicorn freelance_website.wsgi --log-file -
```
4. Deploy:
```bash
heroku create your-app-name
git add .
git commit -m "Initial commit"
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py setup_initial_data
```

### Option 2: DigitalOcean
1. Create Droplet
2. Install Python, Nginx, Gunicorn
3. Configure Nginx
4. Set up SSL with Let's Encrypt

### Option 3: VPS
1. Upload files to server
2. Install dependencies
3. Configure web server (Nginx/Apache)
4. Set up database (PostgreSQL recommended for production)

## 🔒 Security

### Production Checklist
- [ ] Change `SECRET_KEY`
- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use HTTPS
- [ ] Set up database (PostgreSQL)
- [ ] Configure email settings
- [ ] Set up backup system

### Environment Variables
Never commit sensitive information. Use `.env` file:
```env
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

## 📊 Database

### Default: SQLite
- Good for development
- File-based database
- No additional setup required

### Production: PostgreSQL
1. Install PostgreSQL
2. Create database
3. Update settings.py:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🎨 Customization Tips

### Adding New Services
1. Go to Admin Panel → Services
2. Click "Add Service"
3. Fill in details
4. Add FontAwesome icon class
5. Add features as JSON array

### Customizing Styles
Edit `static/css/styles.css`:
- Change colors in CSS variables
- Modify layouts
- Add custom animations

### Adding New Pages
1. Create view in appropriate app
2. Add URL pattern
3. Create template
4. Update navigation

## 🐛 Troubleshooting

### Common Issues

**Static files not loading:**
```bash
python manage.py collectstatic
```

**Database errors:**
```bash
python manage.py makemigrations
python manage.py migrate
```

**Email not working:**
- Check `.env` configuration
- Verify email credentials
- Test with simple email first

**Admin access:**
```bash
python manage.py createsuperuser
```

### Getting Help
- Check Django logs
- Verify file permissions
- Test in development first
- Use Django debug toolbar

## 📈 Performance

### Optimization Tips
- Use CDN for static files
- Optimize images
- Enable caching
- Use database indexing
- Monitor with tools like New Relic

### Monitoring
- Set up logging
- Monitor error rates
- Track page load times
- Set up uptime monitoring

---

**Your Django freelancing website is ready!** 🎉

Start by running the setup commands and then customize the content through the admin panel. 