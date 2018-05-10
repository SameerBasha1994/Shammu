from app import sam,db

from app.models import User,Post

@sam.shell_context_processor
def make_shell_context():
	return {'db':db,'User':User,'Post':Post}