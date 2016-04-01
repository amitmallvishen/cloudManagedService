# Copyright 2015 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.





#################################################################
#################################################################

## Class Name  :  cost_calculation
## Description :  This class contains the core logic to calculate
##                the cost for instances based on physical resouce
##                configuration 

#################################################################
#################################################################

from config_read import InitializationManager
from compute_resources import compute_resource



class cost_calculation( compute_resource ):

    
          def cal_instances_per_node( self , chassis ):
              chassis_config = self.config.CONF.Chassis
              capacity_config = self.config.CONF.OpenStackCapacity
              if 1 == chassis:
                  core_based_on_chassis = chassis_config.chassis_1['core']
                  mem_based_on_chassis = chassis_config_chassis_1['mem']
              elif 2 == chassis:
                  core_based_on_chassis = chassis_config.chassis_2['core']
                  mem_based_on_chassis = chassis_config.chassis_2['mem']
              elif 3 == chassis:
                  core_based_on_chassis = chassis_config.chassis_3['core']
                  mem_based_on_chassis = chassis_config.chassis_3['mem']
              elif 4 == chassis:
                  core_based_on_chassis = chassis_config.chassis_4['core']
                  mem_based_on_chassis = chassis_config.chassis_4['mem']
              elif 5 == chassis:
                  core_based_on_chassis = chassis_config.chassis_5['core']
                  mem_based_on_chassis = chassis_config.chassis_5['mem']
              elif 6 == chassis:
                  core_based_on_chassis = chassis_config.chassis_6['core']
                  mem_based_on_chassis = chassis_config.chassis_6['mem']
              elif 7 == chassis:
                  core_based_on_chassis = chassis_config.chassis_7['core']
                  mem_based_on_chassis = chassis_config.chassis_7['mem']
              elif 8 == chassis:
                  core_based_on_chassis = chassis_config.chassis_8['core']
                  mem_based_on_chassis = chassis_config.chassis_8['mem']
              else:
               # TODO : throw an exception
                  core_based_on_chassis = 0 
              
              cal_ins_per_node1 = ( float(core_based_on_chassis) * float(capacity_config.Hyperthreading_Factor) * float(capacity_config.Memory_Oversubscription_Factor) ) / capacity_config.Average_vCPUs_per_instance
          
              cal_ins_per_node2 = float(mem_based_on_chassis) / capacity_config.Average_memory_per_instance

              return min(cal_ins_per_node1 , cal_ins_per_node2 )



          def cal_number_of_nodes_required( self , chassis ):
              chassis_config = self.config.CONF.Chassis
              capacity_config = self.config.CONF.OpenStackCapacity

              if 1 == chassis:
                  core_based_on_chassis = chassis_config.chassis_1['core']
                  mem_based_on_chassis = chassis_config_chassis_1['mem']
              elif 2 == chassis:
                  core_based_on_chassis = chassis_config.chassis_2['core']
                  mem_based_on_chassis = chassis_config.chassis_2['mem']
              elif 3 == chassis:
                  core_based_on_chassis = chassis_config.chassis_3['core']
                  mem_based_on_chassis = chassis_config.chassis_3['mem']
              elif 4 == chassis:
                  core_based_on_chassis = chassis_config.chassis_4['core']
                  mem_based_on_chassis = chassis_config.chassis_4['mem']
              elif 5 == chassis:
                  core_based_on_chassis = chassis_config.chassis_5['core']
                  mem_based_on_chassis = chassis_config.chassis_5['mem']
              elif 6 == chassis:
                  core_based_on_chassis = chassis_config.chassis_6['core']
                  mem_based_on_chassis = chassis_config.chassis_6['mem']
              elif 7 == chassis:
                  core_based_on_chassis = chassis_config.chassis_7['core']
                  mem_based_on_chassis = chassis_config.chassis_7['mem']
              elif 8 == chassis:
                  core_based_on_chassis = chassis_config.chassis_8['core']
                  mem_based_on_chassis = chassis_config.chassis_8['mem']
              else:
               # TODO : throw an exception
                  core_based_on_chassis = 0 

              cal_number_of_nodes_req1 = self.cal_num_of_instances_for_design() * self.config.CONF.OpenStackCapacity.Average_vCPUs_per_instance / \
                                         ( float(core_based_on_chassis) * float(self.config.CONF.OpenStackCapacity.CPU_Oversubscription_Factor) * self.config.CONF.OpenStackCapacity.Hyperthreading_Factor )

              cal_number_of_node_req2 = self.cal_num_of_instances_for_design() * self.config.CONF.OpenStackCapacity.Average_memory_per_instance / int(mem_based_on_chassis)

              return max ( cal_number_of_nodes_req1 , cal_number_of_node_req2 ) 


          def cal_cost_per_instance( self , chassis ):
              
              chassis_config = self.config.CONF.Chassis

              if 1 == chassis:
                  price_based_on_chassis = chassis_config.chassis_1['price']
              elif 2 == chassis:
                  price_based_on_chassis = chassis_config.chassis_1['price']
              elif 3 == chassis:
                  price_based_on_chassis = chassis_config.chassis_1['price']
              elif 4 == chassis:
                  price_based_on_chassis = chassis_config.chassis_1['price']
              elif 5 == chassis:
                  price_based_on_chassis = chassis_config.chassis_1['price']
              elif 6 == chassis:
                  price_based_on_chassis = chassis_config.chassis_1['price']
              elif 7 == chassis:
                  price_based_on_chassis = chassis_config.chassis_1['price']
              elif 8 == chassis:
                  price_based_on_chassis = chassis_config.chassis_1['price']
              else:
               # TODO : throw an exception
                  price_based_on_chassis = chassis_config.chassis_1['price']

              return float(price_based_on_chassis) / self.cal_instances_per_node( chassis )  
 
if __name__ == "__main__":

    res = compute_resource()
    print "toatal no compute node",res.cal_no_of_compute_node()
    print "total vcpu",res.cal_total_vcpu()
    print "total memory",res. cal_total_memory()
    print "number of instances for design", res.cal_num_of_instances_for_design()
    print "cal_instances_based_on_vcpu",res.cal_instances_based_on_vcpu()
    print "cal_instances_based_on_memory",res.cal_instances_based_on_memory()
 
    chassis = 2
    cos = cost_calculation()
    print "cal cost of ins",cos.cal_instances_per_node( chassis )  
    print "cal number of nodes", cos.cal_number_of_nodes_required( chassis )
    print "cal cost per instance", cos.cal_cost_per_instance( chassis ) 
