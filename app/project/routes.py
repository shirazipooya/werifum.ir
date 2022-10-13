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
    page = request.args.get('page', 1, type=int)
    projects = Project.query.order_by("status").paginate(page=page, per_page=6)
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
    page = request.args.get('page', 1, type=int)
    projects = Project.query.filter_by(status="خاتمه یافته").order_by(Project.title.desc()).paginate(page=page, per_page=6)
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
    page = request.args.get('page', 1, type=int)
    projects = Project.query.filter_by(status="پروپوزال").order_by(Project.title.desc()).paginate(page=page, per_page=6)
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
    page = request.args.get('page', 1, type=int)
    projects = Project.query.filter_by(status="در حال انجام").order_by(Project.title.desc()).paginate(page=page, per_page=6)
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
        flash(message=f"پروژه با موفقیت ایجاد گردید!", category="success")
        return redirect(location=url_for(endpoint="project.project"))
    return render_template("project/create-project.html", form=form)



@bp_project.route("/project/<int:project_id>/update", methods=["GET", "POST"])
@login_required
def project_update(project_id):
    project = Project.query.get_or_404(project_id)
    form = CreateProjectForm()
    if form.validate_on_submit():
        project.title = form.title.data
        project.status = form.status.data
        project.organization = form.organization.data
        project.person = form.person.data
        db.session.commit()
        flash(message="پروژه با موفقیت بروزرسانی گردید!", category="success")
        return redirect(location=url_for(endpoint="project.project"))
    elif request.method == "GET":
        form.title.data = project.title
        form.status.data = project.status
        form.organization.data = project.organization
        form.person.data = project.person
    return render_template("project/update-project.html", form=form)