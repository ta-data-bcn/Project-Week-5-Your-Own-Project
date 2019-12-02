def quantile_label(value):
    if value < 0.26:
        return 'VL'
    elif value < 0.51:
        return 'L'
    elif value < 0.76:
        return 'H'
    else:
        return 'VH'
    
    
    
def quantile_label1(value):
    if value < 26:
        return 'VL'
    elif value < 51:
        return 'L'
    elif value < 76:
        return 'H'
    else:
        return 'VH'
    
    
def first(value,value1):  
    
    if value is 'VL':
        return Vcalm(value1)
        
    elif value is 'L':
        return calm(value1)
              
    elif value is 'H':
        return active(value1)
            
    elif value is 'VH':
        return Vactive(value1)
        
        
def Vcalm(value1):
    
    if value1 is 'VL':
        return 'anxious'
        
    elif value1 is 'L':
        return 'embarassed'
        
    elif value1 == 'H':
        return 'serious' 
    
    elif value1 == 'VH':
        return 'peaceful'
        
        
        
def calm(value1):
    
    if value1== 'VL':
        return 'depressed'
    
    elif value1 == 'L':
        return 'worried'
    
    elif value1 == 'H':
        return 'impressed'
    
    elif value1 == 'VH':
        return 'hopeful'
    
    
def active(value1):
    conds=['VL','L','H','VH']
    
    if value1== 'VL':
        return 'discontented'
    
    elif value1 == 'L':
        return 'distrustful'
    
    elif value1 == 'H':
        return 'passionate'
    
    elif value1 == 'VH':
        return 'happy'
    
    
    
def Vactive(value1):
    conds=['VL','L','H','VH']
    
    if value1== 'VL':
        return 'hateful'
    
    elif value1 == 'L':
        return 'angry and afraid'
    
    elif value1 == 'H':
        return 'ambitious'

    elif value1 == 'VH':
        return 'excited'
        