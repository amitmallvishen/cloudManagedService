
#################################################################
#################################################################

## Class Name  :  dataAdapter
## Description : 
## write desc               

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
