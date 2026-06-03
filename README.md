# Accessory Shop

An online shop built with Django following an HTML-over-the-wire approach using HTMX for dynamic interactions and TailwindCSS for styling.

## Current Status

Project foundation and development environment setup are completed.

Current setup includes:

* Django project structure with apps organized under `apps/`
* Split settings configuration (`base`, `local`, `production`)
* Docker and Docker Compose setup
* PostgreSQL database integration
* Redis integration
* Environment variable management with `.env`
* Ruff and Pre-Commit configuration
* TailwindCSS frontend structure
* Static and template organization
* Git repository initialization

## Tech Stack

### Backend

* Django
* PostgreSQL
* Redis

### Frontend

* HTMX
* TailwindCSS
* Alpine.js
* JavaScript

### Development Tools

* Docker
* Docker Compose
* Ruff
* Pre-Commit
* Git

## Project Structure

```text
accessory-shop/

apps/
config/
frontend/
nodemodules/
requirements/
scripts/
static/
templates/
```

## Running the Project

Start the services:

```bash
docker compose up -d
```

Apply migrations:

```bash
docker compose exec web python manage.py migrate
```

Create a superuser:

```bash
docker compose exec web python manage.py createsuperuser
```

Start Tailwind watcher:

```bash
npx @tailwindcss/cli -i ./frontend/src/css/input.css -o ./static/css/output.css --watch
```

## Environment Variables

Create a `.env` file:

```env
DEBUG=True
SECRET_KEY=change-me

POSTGRES_DB=shop_db
POSTGRES_USER=shop_user
POSTGRES_PASSWORD=change-password
```

## Upcoming Features

* User authentication
* Product catalog
* Categories
* Shopping cart
* Wishlist
* Checkout flow
* Order management
* Payment integration
* Admin customization
* Search and filtering
