import web
from compute_resources import compute_resource


class welcome:
    def GET(self):
        data = web.input()
        print "amit GET method got hit"

        print "data",data.__class__
        res = compute_resource()

        vCpu, memory = res.calc_os_capacity( data )

        print "my calc vcpu " ,vCpu 
        print "my calc memory" ,memory 

        return vCpu,memory


class osCapacity(object):
    def POST(self):
        data = web.input()
        print "amit POST method got hit"

        print "data",data.__class__
        res = compute_resource()

        vCpu, memory = res.calc_os_capacity( data )

        print "my calc vcpu " ,vCpu 
        print "my calc memory" ,memory 

        return vCpu,memory
