from flask import Blueprint, render_template
from flask_login import current_user, login_required



bp_dashboard = Blueprint(
    name='dashboard',
    import_name=__name__
)


@bp_dashboard.route('/')
@login_required
def dashboard():
    return render_template(
        template_name_or_list='dashboard/index.html',
    )

