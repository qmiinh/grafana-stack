import logging, json
import logging.handlers

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address = ('127.0.0.1',51893))

my_logger.addHandler(handler)

debug = '{ "type":"debug" }'
critical = '{ "type":"critical" }'
x = json.loads(debug)
y = json.loads(critical)
my_logger.debug(x)
my_logger.critical(y)