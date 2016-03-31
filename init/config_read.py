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

## Class Name  :  InitializationManager
## Description :  This class will read the configuration file 

#################################################################
#################################################################

from oslo_config import cfg


class InitializationManager(object):

    opt_group = cfg.OptGroup( name = 'OpenStackCapacity' ,
                          title = 'OpenStackConfiguration' )

    capacity_opts = [ cfg.IntOpt( name ='CPUs_per_compute_node', default=2, help=('CPU per compute node')),
                      cfg.IntOpt( name ='Cores_per_CPU', default=12 ,help=('core per cpu') ),
                      cfg.BoolOpt( name ='Hyperthreading' , default='yes' , help=(' hyper threading' )),
                      cfg.IntOpt( name = 'Memory_per_compute_node' , default = 256 , help=('memory per compute node')), 
                      cfg.IntOpt( name = 'Average_vCPUs_per_instance' ,default = 2 , help=('avarage cpu per compute node')), 
                      cfg.IntOpt( name = 'Average_memory_per_instance' , default = 4 , help=('average memory per instance')), 
                      cfg.IntOpt( name = 'Average_ephemeral_per_instance', default = 0 , help=('average ephermal per instance')) , 
                      cfg.IntOpt( name = 'Average_block_storage_per_instance', default = 25 , help=(' average block storage')), 
                      cfg.IntOpt( name = 'Average_IOPS_per_instance', default = 50  , help=('average IOPS per instance')), 
                      cfg.IntOpt( name = 'Current_number_of_instances', default = 6000 , help=(' change number of instance')), 
                      cfg.IntOpt( name = 'Rack_units_per_node', default = 1, help=('rack space per node')), 
                      cfg.FloatOpt( name = 'Hyperthreading_Factor', default = 1.3, help=('hyperthreading factor')), 
                      cfg.IntOpt( name = 'CPU_Oversubscription_Factor', default = 4  , help=('cpu oversubscription factor')), 
                      cfg.IntOpt( name = 'Memory_Oversubscription_Factor', default =1  , help=('memory oversubscription ')), 
                      cfg.IntOpt( name = 'Instance_scaling_over_6_months', default =30  , help=('instance scaling') )
                    ]


    chassis_grp = cfg.OptGroup( name = 'Chassis' ,
                                title = 'OpenStackchassis' )
 
    chassis_opts = [ cfg.DictOpt ( name = 'chassis_1' , default = None , help=('chassis 1') ),
                     cfg.DictOpt ( name = 'chassis_2' , default = None , help=('chassis 2') ),
                     cfg.DictOpt ( name = 'chassis_3' , default = None , help=('chassis 3') ),
                     cfg.DictOpt ( name = 'chassis_4' , default = None , help=('chassis 4') ),
                     cfg.DictOpt ( name = 'chassis_5' , default = None , help=('chassis 5') ),
                     cfg.DictOpt ( name = 'chassis_6' , default = None , help=('chassis 6') ),
                     cfg.DictOpt ( name = 'chassis_7' , default = None , help=('chassis 7') ),
                     cfg.DictOpt ( name = 'chassis_8' , default = None , help=('chassis 8') )
                    ]

    def __init__( self ):
       self.CONF = cfg.CONF
       self.CONF.register_group( self.opt_group )
       self.CONF.register_opts( self.capacity_opts , self.opt_group )
       self.CONF.register_group( self.chassis_grp )
       self.CONF.register_opts( self.chassis_opts , self.chassis_grp )
