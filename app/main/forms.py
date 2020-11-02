from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    title = StringField('Title')
    description = TextAreaField('Description', validators=[Required()])
    category = SelectField('Type', choices=[('conference', 'Conference pitch'),('sales','Sales pitch'),('social','Social pitch')],validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Write a comment', validators=[Required()])
    submit = SubmitField('Comment')
