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

## Class Name  :  compute_resource
## Description :  This class contains the core logic to calculate
##                the resouces need to estimated

#################################################################
#################################################################

from myapplication import myapplication
from data_adapter import dataAdapter 
from config_read import InitializationManager
from oslo_log import log as logging


LOG = logging.getLogger(__name__)



class compute_resource(myapplication):

      config = InitializationManager()
      config.CONF( default_config_files = ['conf/openstackconfiguration.conf'] )


      def __init__( self ):
          config = InitializationManager()
          config.CONF ( default_config_files = ['conf/openstackconfiguration.conf'] )
          self.db_dict = dict( config.CONF.OpenStackCapacity )

######################################################
      def update_config_db( self ,config_dict ):

          print "update_config_db"
          for key in self.db_dict:
              print "my local dict key's value : ",self.db_dict[key]," type of value : ", type(self.db_dict[key])

          data_adapter = dataAdapter( config_dict , self.db_dict )
          if True == data_adapter.dirty:
             print " object is dirty"
          else:
             print " object is clean"
              # raise exception : raise ValueError: 

          for key in self.db_dict:
              print "my key updated value : ",self.db_dict[key]
####################################################

      def cal_num_of_instances_for_design( self ):
          return ( (self.db_dict['Current_number_of_instances']) * (( 100 + self.db_dict['Instance_scaling_over_6_months'] ) /float(100) )) 


      def cal_no_of_compute_node( self ):

          no_compute_node = ( self.db_dict['Average_vCPUs_per_instance'] * self.cal_num_of_instances_for_design()  / \
                              ( self.db_dict['CPUs_per_compute_node'] * self.db_dict['Cores_per_CPU'] *  \
                                self.db_dict['Hyperthreading_Factor'] * self.db_dict['CPU_Oversubscription_Factor'] ) )

          no_compute_node1 = self.db_dict['Average_memory_per_instance'] * self.cal_num_of_instances_for_design() / float(self.db_dict['Memory_per_compute_node'])

          return round(max(no_compute_node , no_compute_node1 ) )

      def cal_total_vcpu( self ):

          if True == self.db_dict['Hyperthreading']:
              print "self.db_dict : True",self.db_dict['Hyperthreading']

              total_vcpu = self.cal_no_of_compute_node() * self.db_dict['CPUs_per_compute_node'] * \
                           self.db_dict['Cores_per_CPU'] * self.db_dict['Hyperthreading_Factor'] * self.db_dict['CPU_Oversubscription_Factor']
          else:
              print "self.db_dict : False",self.db_dict['Hyperthreading']
              total_vcpu = self.cal_no_of_compute_node() * self.db_dict['CPUs_per_compute_node'] * \
                           self.db_dict['Cores_per_CPU'] * self.db_dict['CPU_Oversubscription_Factor']


          print "what is upadted val",self.db_dict['Cores_per_CPU']
          return total_vcpu


      def cal_total_memory( self ):
           
          total_mem = self.cal_no_of_compute_node() * self.db_dict['Memory_per_compute_node']

          return total_mem

    
      def cal_instances_based_on_vcpu( self ):
 
         return	self.cal_total_vcpu() / self.db_dict['Average_vCPUs_per_instance']

 
      def cal_instances_based_on_memory ( self ):
         return self.cal_total_memory() / self.db_dict['Average_memory_per_instance']


      def calc_os_capacity( self , config_dict = None):
          if config_dict != None:
             self.update_config_db( config_dict )

          vcpu = self.cal_instances_based_on_vcpu()
          memory = self.cal_instances_based_on_memory()

          return vcpu,memory
 
#if __name__ == "__main__":

#    res = compute_resource()
#    print "toatal no compute node",res.cal_no_of_compute_node()
#    print "total vcpu",res.cal_total_vcpu()
#    print "total memory",res. cal_total_memory()
#    print "number of instances for design", res.cal_number_of_instance_for_design()
#    print "cal_instances_based_on_vcpu",res.cal_instances_based_on_vcpu()

#    print "cal_instances_based_on_memory",res.cal_instances_based_on_memory() 

