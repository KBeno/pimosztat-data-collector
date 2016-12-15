from optparse import OptionParser
import random
from time import sleep
from datetime import datetime

def get_random_values():
    humidity = round(random.uniform(20, 80),1)
    temperature = round(random.uniform(15, 25),1)
    return {"humidity": humidity, "temperature": temperature}

def get_real_value(type, pin):
    # TODO
    return get_random_values()

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="output file name", metavar="FILE")
parser.add_option("-t", "--type", dest="type", help="sensor type", default=22, metavar="INT")
parser.add_option("-p", "--pin", dest="pin", help="GPIO pin", default=4, metavar="INT")
parser.add_option("-d", "--demo", dest="demo", help="demo mode", default=False, action="store_true")

(options, args) = parser.parse_args()

if not hasattr(options, "filename"):
    parser.error("--file is mandatory")

while True:
    time_stamp = datetime.now().isoformat()
    if options.demo:
        result = get_random_values()
        sleep(1)
    else:
        try:
            result = get_real_value(options.type, options.pin)
        except Exception as e:
            print ("Failed to get sensor data. "+str(e))
        sleep(60)
    print(result)
    with open(options.filename, "a") as output:
        output.write("{timestamp}, {humidity}, {temp}\n".format(timestamp=time_stamp, humidity=result['humidity'],
                                                            temp=result['temperature']))
