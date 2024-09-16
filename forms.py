from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, SelectField, MultipleFileField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField
from flask_babel import _


TYPE_CHOICES = [('a', _('Apartment')), ('h', _('House')), ('p', _('Plot'))]
CURRENCY_CHOICES = [('eur', 'EUR'), ('usd', 'USD'), ('bgn', 'BGN')]

# WTForm for creating a property add
class AddPropertyForm(FlaskForm):
    price = IntegerField(_("Price"), validators=[DataRequired()])
    currency = SelectField(_("Currency"), validators=[DataRequired()], choices=CURRENCY_CHOICES)
    city_lantin = StringField(_("City"), validators=[DataRequired()])
    city_cyrillic = StringField(_("City Cyrillic"), validators=[DataRequired()])
    area_lantin = StringField(_("District Latin"), validators=[DataRequired()])
    area_cyrillic = StringField(_("District Cyrillic"), validators=[DataRequired()])
    type = SelectField(_("Property Type"), validators=[DataRequired()], choices=TYPE_CHOICES)
    size = IntegerField(_("Size"), validators=[DataRequired()])
    bedrooms = IntegerField(_("Bedrooms"))
    bathrooms = IntegerField(_("Bathrooms"))
    description_en = CKEditorField(_("Description English"))
    description_bg = CKEditorField(_("Description Bulgarian"), validators=[DataRequired()])
    description_ru = CKEditorField(_("Description Russian"))
    pics = MultipleFileField(_("Pictures"), render_kw={"multiple": True})
    upload_pics = SubmitField(_("Upload Pictures"))
    submit = SubmitField(_("Add property"))


# Create a form to login existing users
class LoginForm(FlaskForm):
    username = StringField(_("Username"), validators=[DataRequired()])
    password = PasswordField(_("Password"), validators=[DataRequired()])
    submit = SubmitField(_("Login"))

# Create a form to register new users
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")