from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('describe yourself',validators = [DataRequired()])
    submit = SubmitField('save')

class PitchForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    category = SelectField('category', choices=[('Jobs','Jobs'),('Event','Event'),('Dates','Dates')],validators=[DataRequired()])
    post = TextAreaField('your pitch', validators=[DataRequired()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('comment',validators=[DataRequired()])
    submit = SubmitField('comment')