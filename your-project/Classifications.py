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
        return 'anxious and weakness'
        
    elif value1 is 'L':
        return 'embarassed and doubtful'
        
    elif value1 == 'H':
        return 'serious and polite' 
    
    elif value1 == 'VH':
        return 'peaceful and friendly'
        
        
        
def calm(value1):
    
    if value1== 'VL':
        return 'depressed and miserably uncomfortable'
    
    elif value1 == 'L':
        return 'worried and feeling guilt'
    
    elif value1 == 'H':
        return 'impressed and attentive'
    
    elif value1 == 'VH':
        return 'hopeful and pleased'
    
    
def active(value1):
    conds=['VL','L','H','VH']
    
    if value1== 'VL':
        return 'discontented and disgusted'
    
    elif value1 == 'L':
        return 'distrustful and indignant'
    
    elif value1 == 'H':
        return 'passionate and light hearted'
    
    elif value1 == 'VH':
        return 'happy and determined'
    
    
    
def Vactive(value1):
    conds=['VL','L','H','VH']
    
    if value1== 'VL':
        return 'hateful and disrespectful'
    
    elif value1 == 'L':
        return 'angry, alarmed and afraid'
    
    elif value1 == 'H':
        return 'ambitious and feeling superior'

    elif value1 == 'VH':
        return 'excited and courageous'
        