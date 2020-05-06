from flask import render_template

from . import sandbox


@sandbox.route('/sandbox')
def sandbox_evaluate():
    return render_template('sandbox/sandbox.html')
