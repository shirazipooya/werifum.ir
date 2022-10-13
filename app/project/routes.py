from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from app.project.models import Project
from app.project.forms import CreateProjectForm
from app.extensions import db


bp_project = Blueprint(
    name='project',
    import_name=__name__
)


@bp_project.route('/project')
@login_required
def project():
    num = Project.query.order_by("status").all()
    projects = Project.query.order_by("status").all()
    return render_template(
        template_name_or_list="project/index.html",
        projects=projects,
        num=num,
        page_name="all"
    )


@bp_project.route('/project/done')
@login_required
def project_done():
    num = Project.query.order_by("status").all()
    projects = Project.query.filter_by(status="خاتمه یافته").order_by(Project.title.desc()).all()
    return render_template(
        template_name_or_list="project/index.html",
        projects=projects,
        num=num,
        page_name="done"
    )


@bp_project.route('/project/proposal')
@login_required
def project_proposal():
    num = Project.query.order_by("status").all()
    projects = Project.query.filter_by(status="پروپوزال").order_by(Project.title.desc()).all()
    return render_template(
        template_name_or_list="project/index.html",
        projects=projects,
        num=num,
        page_name="proposal"
    )


@bp_project.route('/project/in-progress')
@login_required
def project_in_progress():
    num = Project.query.order_by("status").all()
    projects = Project.query.filter_by(status="در حال انجام").order_by(Project.title.desc()).all()
    return render_template(
        template_name_or_list="project/index.html",
        projects=projects,
        num=num,
        page_name="in_progress"
    )



@bp_project.route("/project/create", methods=["GET", "POST"])
def create_project():    
    form = CreateProjectForm()
    if form.validate_on_submit():
        project = Project(
            title=form.title.data,
            status=form.status.data,
            organization=form.organization.data,
            person=form.person.data,
        )
        db.session.add(project)
        db.session.commit()
        flash(message=f"Project Created Successfully!", category="success")
        return redirect(location=url_for(endpoint="project.project"))
    return render_template("project/create-project.html", form=form)