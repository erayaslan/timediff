from datetime import datetime

from flask import Flask, redirect, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect, FlaskForm
from wtforms.fields import DateTimeLocalField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "WdeIkz+D2qXx08hqcxtEukfGUfZHuNTD+M/DRAZN"

# set default button sytle and size, will be overwritten by macro parameters
app.config["BOOTSTRAP_BTN_STYLE"] = "primary"
app.config["BOOTSTRAP_BTN_SIZE"] = "sm"
app.config["BOOTSTRAP_BOOTSWATCH_THEME"] = "spacelab"

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)


class DateForm(FlaskForm):
    """A simple form that is used to get a date"""

    initial_date = DateTimeLocalField(
        format="%Y-%m-%dT%H:%M",
        description="""Enter your birthday
            with time in UTC if you want to be precise""",
        validators=[DataRequired()],
    )
    submit = SubmitField()


@app.route("/", methods=["GET"])
def index():
    form = DateForm()
    return render_template("index.html", form=form)


@app.route("/", methods=["POST"])
def results():
    form = DateForm()
    if form.validate_on_submit():
        now = datetime.utcnow()
        _diff = now - form.initial_date.data
        diff_years = f"{_diff.days/365.2425:,.2f}"
        diff_days = f"{_diff.days:,}"
        diff_seconds = f"{_diff.days * 86400 + _diff.seconds:,}"
        return render_template(
            "index.html", form=form, diff=[diff_years, diff_days, diff_seconds]
        )
    return redirect(request.url)


if __name__ == "__main__":
    app.run(debug=True)
