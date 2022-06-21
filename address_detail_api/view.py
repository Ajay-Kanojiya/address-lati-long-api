from address_detail_api import api
from address_detail_api.control import get_address_detials
from flask_restx import Resource, reqparse

# swagger documentaion details.
parser = reqparse.RequestParser()
parser.add_argument(name="address", type=str, location="form", trim=True, required=True)
parser.add_argument(name="output_format", type=str, location="form", default="json", case_sensitive=False, trim=True)
ns = api.namespace(name="", description="Methods available in the address details API are listed below.")


# route for fetching the address details.
@ns.route("/getAddressDetails")
class GetAddressDetails(Resource):
    @api.doc(parser=parser)
    def post(self):
        try:
            args = parser.parse_args()
            return get_address_detials(args.get("address"), args.get("output_format"))
        except Exception:
            pass
