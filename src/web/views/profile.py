from flask import render_template

from flask.ext.login import login_required

@login_required
def show():
    # user_id = current_user.id
    # donations = db.session.query(Donation).filter_by(user_id=123).all()
    # return render_template('profile/show.tmpl', donations=donations)
    return render_template('profile/show.tmpl')
