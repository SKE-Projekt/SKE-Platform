import json
from flask import render_template, Response, request
from flask_login import login_required

from . import sandbox
from .forms import SandboxCodeForm
from .actions import SandboxExecutor


@sandbox.route('/sandbox')
def sandbox_evaluate():
    form = SandboxCodeForm()
    return render_template('sandbox/sandbox.html', form=form)

@sandbox.route('/sandbox/api/evaluate', methods=['POST', 'GET'])
@login_required
def evalute_code():
    data = {}
    form = SandboxCodeForm(request.form)
    if form.validate():
        code = "\n".join(form.code.data.split("</br>"))
        input_data = "\n".join(form.input_data.data.split("</br>"))

        exctr = SandboxExecutor(code, input_data)
        exctr.run()

        if exctr.return_code != 0:
            data = {
                'msg': exctr.output_data.split('\n')[-2],
                'code': exctr.return_code
            }
        else:
            data = {
                'msg': exctr.output_data,
                'code': exctr.return_code
            }
    else:
        data = {
            'msg': 'Sprawdź, czy twój kod/wejście nie jest za duże.',
            'code': 2138
        }
    return data
