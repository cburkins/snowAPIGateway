from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Incident(Resource):

	# Parser belongs to the class, not any particular item (instance)
	parser = reqparse.RequestParser()

	parser.add_argument('count',
		type=int, 
		required=True,
		help="How many incidents do you want ?"
	)

	# - - - - - - - - - - - - - - 
	# GET
	def get(self, count):


		return {'message': 'Apparently you want %s incidents ?' % (count)}, 200

# --------------------------------------------------------------------------------------------

class IncidentList(Resource):
	def get(self):
		# Both of these work
		return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
		#return {'items': [item.json() for item in ItemModel.query.all()]}

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
