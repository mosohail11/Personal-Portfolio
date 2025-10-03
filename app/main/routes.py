from flask import render_template

from . import main_bp


@main_bp.get("/")
def home():
    return render_template("home.html")


@main_bp.get("/projects")
def projects():
    return render_template("projects.html")


@main_bp.get("/projects/<string:slug>")
def project_detail(slug: str):
    return render_template("project_detail.html", slug=slug)


@main_bp.get("/skills")
def skills():
    return render_template("skills.html")


@main_bp.get("/about")
def about():
    return render_template("about.html")


@main_bp.get("/contact")
def contact():
    return render_template("contact.html")
