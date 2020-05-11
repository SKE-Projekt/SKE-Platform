from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length


class SandboxCodeForm(FlaskForm):
    code = StringField(validators=[Length(max=128 * 1222, message='Kod musi być krótszy!')])
    input_data = StringField(validators=[Length(max=128 * 128, message='Wejście musi być mniejsze!')])
