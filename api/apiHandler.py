import web
from compute_resources import compute_resource
import json



class welcome:
    def GET(self):
        data = web.input()
        print "amit GET method got hit"

        print "data",data.__class__
        res = compute_resource()

        vCpu, memory = res.calc_os_capacity( data )

        print "my calc vcpu " ,vCpu 
        print "my calc memory" ,memory 

        s1 = str(vCpu)
        s2 = str(memory)
        data = {}
         
        data['vCpu'] = s1 
        data['memory'] = s2


        json_data = json.dumps(data)#{ 'vCpu' : '' , 'memory' :'' })
 
        return json_data


class osCapacity(object):
    def POST(self):
        data = web.input()
        print "amit POST method got hit"

        print "data",data.__class__
        res = compute_resource()

        vCpu, memory = res.calc_os_capacity( data )

        print "my calc vcpu " ,vCpu 

        print "my calc memory" ,memory

        s1 = str(vCpu)
        s2 = str(memory)
        data = {}
         
        data['vCpu'] = s1 
        data['memory'] = s2


        json_data = json.dumps(data)#{ 'vCpu' : '' , 'memory' :'' })
 
        return json_data
