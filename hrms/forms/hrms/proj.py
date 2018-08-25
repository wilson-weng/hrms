from ...forms.base_form import BaseForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Optional


class ProjUpdateForm(BaseForm):
    company_id = IntegerField('company_id', validators=[DataRequired()])
    proj_name = StringField('proj_name', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    crew_num = IntegerField('crew_num', validators=[DataRequired()])
    category = IntegerField('category', validators=[DataRequired()])
    pic_url_list = StringField('pic_url_list', validators=[Optional()])
