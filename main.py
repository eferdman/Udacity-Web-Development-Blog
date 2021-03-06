import webapp2
from helper import *

form="""
<form method = "post">
	What is your birthday?
	<br>
	<label>Month <input type="text" name="month"></label>
	<label>Day <input type="text" name="day"></label>
	<label>Year <input type="text" name="year"></label>
	<div style="color: red">%(error)s</div>
	<br>
	<br>
	<input type = "submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
	def write_form(self, error=""):
		self.response.out.write(form % {"error": error})

	def get(self):
		#self.response.headers['Content-Type'] = 'text/plain'
		self.write_form()

	def post(self):
		user_month = valid_month(self.request.get('month'))
		user_day = valid_day(self.request.get('day'))
		user_year = valid_year(self.request.get('year'))

		if not (user_month and user_day and user_year):
			self.write_form("That doesn't look valid to me, friend.")
		else:
			self.response.out.write("Thanks! That's totes a great bday!")

app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
