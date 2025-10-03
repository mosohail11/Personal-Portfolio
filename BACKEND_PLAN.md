# Backend Development Plan

App name: Personal portfolio
Stack: Flask (Python), HTML/CSS/Tailwind/JS, SQLite + SQLAlchemy

## Goals
- Keep backend modular, readable, and easy to extend
- Separate router per module via Flask blueprints
- Prepare for future dynamic features while Step 1 remains static-rendered

## Architecture
- `app/`
  - `__init__.py`: app factory, register blueprints
  - `main/`: static pages (home, projects, skills, about, contact)
  - `projects/`: future dynamic projects CRUD, listing, detail
  - `contact/`: future contact form submission and email sending
  - `common/`: shared utilities, config, error handlers
  - `models.py`: SQLAlchemy models
  - `extensions.py`: db, migrate, and other extension init
- `templates/`, `static/`: Jinja templates and assets

## Blueprints (Routers)
- `main_bp` (`/`): static pages
- `projects_bp` (`/projects`): list, detail (future: filter, tags)
- `contact_bp` (`/contact`): form submit API, rate-limit (future)

## Models
- `Project`: id, slug, title, summary, tech_stack (JSON), impact (JSON), github_url, demo_url, created_at
- `Skill`: id, name, level (Proficient/Familiar/Target), category

## Config
- Envs: `FLASK_ENV`, `DATABASE_URL` (default sqlite `instance/app.db`)
- CSRF secret key for forms when made dynamic

## APIs (Future)
- `GET /api/projects`: list projects (paginate)
- `GET /api/projects/<slug>`: detail
- `POST /api/contact`: submit contact form (captcha + email notification)

## Validation & Security
- Use `wtforms` or `pydantic`-style validation for inputs
- Rate limit `POST /api/contact`
- Sanitize HTML output via Jinja autoescape

## Testing
- Pytest for routes and models
- In-memory SQLite for unit tests

## Migrations
- Use `Flask-Migrate` for schema changes

## Deployment
- Gunicorn/Uvicorn (if needed) behind Nginx (or render.com/railway.app)
- Containerize with Docker; use multi-stage build

## Roadmap
1. Step 1 (done): static screens with Flask templates
2. Add `extensions.py` with SQLAlchemy and migrate
3. Implement `Project`/`Skill` models and seed script
4. Make Projects/Skills dynamic from DB
5. Implement contact form POST + email (e.g., SendGrid)
6. Add sitemap, SEO tags, OpenGraph, analytics
