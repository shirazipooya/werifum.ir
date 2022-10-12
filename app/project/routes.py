from flask import Blueprint, render_template
from flask_login import current_user, login_required



bp_project = Blueprint(
    name='project',
    import_name=__name__
)


@bp_project.route('/project')
@login_required
def project():
    return render_template(
        template_name_or_list='project/index.html',
    )