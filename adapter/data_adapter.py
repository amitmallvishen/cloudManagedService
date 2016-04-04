
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

## Class Name  :  dataAdapter
## Description : 
##                

#################################################################
#################################################################

from myapplication import myapplication

class dataAdapter(myapplication):

  
     def __init__( self , data, class_compute_obj_db_dict ):
         self.data = data
         self.dirty = False
         try:
             for key in data:
#                print "key of data_cfg:",key," type of key :",type(key)," Value of cfg key :",data[key]," type of value cfg : ",type(data[key])
                if key not in class_compute_obj_db_dict.keys():
                #  raise "KeyError" # TODO : for now throwing value error. but later on this will be replaced by actual 
                                      # customized exception class for eg :  KeyError
                    continue
                valueType = type(class_compute_obj_db_dict[key])
                class_compute_obj_db_dict[key] = valueType(data[key]) 
                #if type(data[key]) != type(class_compute_obj_db_dict[key]):
                # TODO 
                # raise "ValueTypeError"
                #    continue

                 
         except ValueError:
              print "Valueconvserion error occured, please check the input data"
              self.dirty = True
              #raise ValueError:
