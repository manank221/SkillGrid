#!/usr/bin/env python3
"""
Simple script to run the Django freelancing website
"""
import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed!")
        print(f"Error: {e.stderr}")
        return False

def main():
    print("🚀 Starting Django Freelancing Website Setup...")
    
    # Check if we're in the right directory
    if not Path("manage.py").exists():
        print("❌ Error: manage.py not found. Please run this script from the project root directory.")
        sys.exit(1)
    
    # Check if virtual environment is activated
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Warning: Virtual environment not detected. It's recommended to use one.")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(0)
    
    # Install requirements
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        print("❌ Failed to install dependencies. Please check your Python environment.")
        sys.exit(1)
    
    # Check if .env file exists
    if not Path(".env").exists():
        print("📝 Creating .env file from template...")
        if Path("env_example.txt").exists():
            with open("env_example.txt", "r") as f:
                env_content = f.read()
            with open(".env", "w") as f:
                f.write(env_content)
            print("✅ .env file created. Please edit it with your settings.")
        else:
            print("⚠️  No env_example.txt found. Creating basic .env file...")
            with open(".env", "w") as f:
                f.write("SECRET_KEY=django-insecure-change-this-in-production\nDEBUG=True\nALLOWED_HOSTS=localhost,127.0.0.1\n")
    
    # Run migrations
    if not run_command("python manage.py makemigrations", "Creating database migrations"):
        print("❌ Failed to create migrations.")
        sys.exit(1)
    
    if not run_command("python manage.py migrate", "Applying database migrations"):
        print("❌ Failed to apply migrations.")
        sys.exit(1)
    
    # Set up initial data
    if not run_command("python manage.py setup_initial_data", "Setting up initial data"):
        print("⚠️  Failed to set up initial data. You can run this manually later.")
    
    # Collect static files
    if not run_command("python manage.py collectstatic --noinput", "Collecting static files"):
        print("⚠️  Failed to collect static files. You can run this manually later.")
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit .env file with your email settings")
    print("2. Run: python manage.py runserver")
    print("3. Visit: http://127.0.0.1:8000/")
    print("4. Admin panel: http://127.0.0.1:8000/admin/")
    print("   Username: admin, Password: admin123")
    
    # Ask if user wants to start the server
    response = input("\n🚀 Start the development server now? (y/n): ")
    if response.lower() == 'y':
        print("\n🌐 Starting Django development server...")
        print("📱 Visit: http://127.0.0.1:8000/")
        print("🔧 Admin: http://127.0.0.1:8000/admin/")
        print("⏹️  Press Ctrl+C to stop the server")
        try:
            subprocess.run("python manage.py runserver", shell=True)
        except KeyboardInterrupt:
            print("\n👋 Server stopped. Goodbye!")
    else:
        print("\n👋 Setup complete! Run 'python manage.py runserver' when ready.")

if __name__ == "__main__":
    main() 