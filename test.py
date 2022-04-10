from lambda_function import *
from test_event import *
event = CSV_PUT

# event = XML_PUT

lambda_handler(event, "")
