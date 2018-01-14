from werkzeug.security import safe_str_cmp
# this is our own Class
from models.user import UserModel

# user gives username and password, we verify same, then give back JTW token
def authenticate(username, password):
	user = UserModel.find_by_username(username)
	if user and safe_str_cmp(user.password, password):
		return user

# User provides JWT token, we match to authorized user
def identity(payload):
	user_id = payload['identity']
	return UserModel.find_by_id(user_id)
