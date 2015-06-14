import webapp2
from helper import *

form="""
<form method = "post">
	What is your birthday?
	<br>
	<label>
		Month 
		<input type="text" name="month" value="%(month)s">
	</label>
	<label>
		Day 
		<input type="text" name="day" value="%(day)s">
	</label>
	<label>
		Year 
		<input type="text" name="year" value="%(year)s">
	</label>
	<div style="color: red">%(error)s</div>
	<br>
	<br>
	<input type = "submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
	def write_form(self, error="", month="", day="", year=""):
		self.response.out.write(form % {"error": error, 
										"month": month, 
										"day": day, 
										"year": year})


	def get(self):
		#self.response.headers['Content-Type'] = 'text/plain'
		self.write_form()

	def post(self):
		#variables for what the user entered
		user_month = self.request.get('month')
		user_day = self.request.get('day')
		user_year = self.request.get('year')

		month = valid_month(user_month)
		day = valid_day(user_day)
		year = valid_year(user_year)

		if not (month and day and year):
			self.write_form("That doesn't look valid to me, friend.", 
							user_month, user_day, user_year)
		else:
			self.response.out.write("Thanks! That's totes a great bday!")

app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
