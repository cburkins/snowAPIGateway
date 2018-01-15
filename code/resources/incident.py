from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from snowAPI import getTableFields, getParamsFromFile
import os
import sys

class Incident(Resource):

    # Parser belongs to the class, not any particular item (instance)
    parser = reqparse.RequestParser()

    parser.add_argument('count',
        type=int, 
        required=True,
        help="How many incidents do you want ?",
        location='args'
    )

    parser.add_argument('verbose',
        type=str, 
        required=False,
        default=False,
        help="this is the verbose flag ?",
        location='args'
    )

    # - - - - - - - - - - - - - - 
    # GET
    def get(self):
        
        args = Incident.parser.parse_args()
        print("\n\nargs: %s\n\n" % (args))

        # Config file name (has access tokens) and add full-path directory name
        configFileName="queryInstance.config"
        configFileFullPath=os.path.join(sys.path[0], configFileName)

        # Read the entire config file (which stores OAuth keys, etc)
        configDict = getParamsFromFile(configFileFullPath);
        currentProfile = configDict["devOne"]
        print(currentProfile);

        profile=currentProfile
        tableName = "incident"
        rowLimit = 5;
        desiredFields = ["opened_at", "short_description", "assigned_to.name", "priority", "u_status", "number"]
        agoUnits = "days"
        agoCount = 3    
        sysparm_query = "sysparm_display_value=true&sysparm_query=ORDERBYDESCopened_at^sys_created_on>=javascript:gs.%sAgoStart(%s)^u_stateNOT IN800,900^priority!=4" % (agoUnits, agoCount)

        JSONresults = getTableFields(profile, tableName, rowLimit, desiredFields, sysparm_query)

        print ("------> %s" % (JSONresults))
        # print("Content-Type: application/json\n");
        # print (JSONresults)
        #return {'message': 'Apparently you want %s incidents ?' % (count)}, 200
        return JSONresults, 200

# --------------------------------------------------------------------------------------------

class IncidentList(Resource):
    def get(self):
        # Both of these work
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
        #return {'items': [item.json() for item in ItemModel.query.all()]}

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
