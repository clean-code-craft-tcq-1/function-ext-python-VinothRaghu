battery_allowedValues = {
           		        'temperature': {'min': 0, 'max': 45},
            		    'state_of_charge': {'min': 20, 'max': 80},
            		    'charge_rate': {'min': 0,'max': 0.8}
                        } 

Display_Message       = {
				'low_breach':   { 'DE' : 'Untergrenze überschritten für ', 
                                                  'EN' : 'Lower Limit Breached for ' }   ,
                                'warning_L' : 	{ 'DE' : 'Unterer Schwellenwert nähert sich '  ,   
                                                  'EN' : 'Lower Threshold Nearing '},
                                'high_breach' : { 'DE' : 'Obergrenze überschritten für '  , 
                                                  'EN' : 'Higher Limit Breached for ' }   ,
                                'warning_H'   : { 'DE' : 'Höhere Schwelle nähert sich ', 
                                                  'EN' : 'Higher Threshold Nearing ' } } 

Temp_unit            = {
                          'C': 'Celsius',
                          'F': 'Fahrenheit'
                       }
			
Lang = "EN"    
                  
def lower_limit(value):
	allowed_limit = 5
	return (value * allowed_limit) / 100
	
status = True
def battery_status():
	return status
	
def rangeValidation(bmsParam_value,bmsParam_name,Lang):
	bottom_level= battery_allowedValues[bmsParam_name]['min']
	high_level = battery_allowedValues[bmsParam_name]['max']
	threshold = lower_limit(high_level)
	lower_value = bottom_level+threshold
	high_value =  high_level-threshold
	if (bmsParam_value < lower_value):
	   print(Display_Message['warning_L'][Lang]+bmsParam_name)
	if (bmsParam_value > high_value):
	   print(Display_Message['warning_H'][Lang]+bmsParam_name)

def battery_Limit_Check(bmsParam_name,bmsParam_value,Lang):
    if (bmsParam_value < battery_allowedValues[bmsParam_name]['min']):
	    print(Display_Message['low_breach'][Lang]+bmsParam_name)
	    status=False
    elif(bmsParam_value > battery_allowedValues[bmsParam_name]['max']):
        print(Display_Message['high_breach'][Lang]+bmsParam_name)
        status=False
    else:
        rangeValidation(bmsParam_value,bmsParam_name,Lang) 
			
def fahrenheit_to_celsius(bmsParam_name,bmsParam_value):
    if (Temp_unit == 'F'):
        Celsius_Value = (bmsParam_value-32)*(5/9)
    else:
        Celsius_Value = bmsParam_value
    return Celsius_Value
                   
def battery_is_ok(temperature,state_of_charge,charge_rate,Lang):
    battery_Limit_Check('temperature',temperature,Lang)
    battery_Limit_Check('state_of_charge',state_of_charge,Lang)
    battery_Limit_Check('charge_rate',charge_rate,Lang)
    return battery_status()

if __name__ == '__main__':
    assert(battery_is_ok(15,65,0.6,'EN') == True)  
    assert(battery_is_ok(15,65,0.6,'DE') == True)
