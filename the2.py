def is_intersect(lower_block,upper_block):
    if upper_block[2] < lower_block[0] < upper_block[0] or upper_block[2] < lower_block[2] < upper_block[0] or lower_block[2] < upper_block[0] < lower_block[0] or lower_block[2] < upper_block[2] < lower_block[0]:
        return True
    else:
        return False
def damnare_intersect(lower_block,upper_block,y_ranges):
    
    else:
        area_upper = abs(upper_block[0] - upper_block[2]) * abs(upper_block[1] - upper_block[3])
        area_lower = abs(lower_block[0] - lower_block[2]) * abs(lower_block[1] - lower_block[3])
def is_firmus(upper_block,lower_block):
    if upper_block[0] < upper_block[2]: #list x dcreasing order
        temp1 = upper_block[0]
        upper_block[0] = upper_block[2]
        upper_block[2] = temp1
        temp2 = upper_block[1]
        upper_block[1] = upper_block[3]
        upper_block[3] = temp2
    if lower_block[0] < lower_block[2]:
        temp1 = lower_block[0]
        lower_block[0] = lower_block[2]
        lower_block[2] = temp1
        temp2 = lower_block[1]
        lower_block[1] = lower_block[3]
        lower_block[3] = temp2
    y1 = upper_block[1] if upper_block[1] > upper_block[3] else upper_block[3] #big y of the upper
    y2 = lower_block[1] if lower_block[1] > lower_block[3] else lower_block[3] #big y of lower
    y3 = upper_block[1] if upper_block[1] < upper_block[3] else upper_block[3] #low of upper
    y4 = lower_block[1] if lower_block[1] < lower_block[3] else lower_block[3] #low of lower
    y_ranges = [y1,y2,y3,y4]
    if y1 < y2:#which one is top box
        templist = []
        templist[:] = upper_block[:]
        upper_block[:] = lower_block[:]
        lower_block[:] = templist[:]
    upper_center_of_mass_point = (upper_block[0] + upper_block[2])/2
    area_upper = abs(upper_block[0] - upper_block[2]) * abs(upper_block[1] - upper_block[3])
    area_lower = abs(lower_block[0] - lower_block[2]) * abs(lower_block[1] - lower_block[3])
    if abs(y4) < 0.001 : #check if lower on the ground
        if is_intersect(lower_block,upper_block):#check if upper on lower
            if abs(y3 - y2) < 0.001: #checks if touching the boxes
                if lower_block[2] - 0.001 < upper_center_of_mass_point < lower_block[0] + 0.001: #checks balance
                    return ['FIRMUS',area_lower+area_upper]
                else:
                    add_block = [0,0,0,0]
                    if upper_center_of_mass_point < lower_block[2] + 0.001: #sola dusecek
                        distance = abs(lower_block[2] - upper_block[2]) - abs(upper_block[0] - lower_block[2])
                        add_block[2] = upper_block[0] + abs(distance)
                        add_block[1] = upper_block[1]
                        add_block[0] = upper_block[0]
                        add_block[3] = upper_block[3]
                        return ['ADDENDUM',add_block]
                    else:#saga dsecek
                        distance = abs(upper_block[0] - lower_block[0]) - abs(lower_block[0] - upper_block[2])
                        add_block[2] = upper_block[2] - abs(distance)
                        add_block[1] = upper_block[1]
                        add_block[0] = upper_block[2]
                        add_block[3] = upper_block[3]
                        return ['ADDENDUM',add_block]
            else:#boxs is not top to top but may intersect
                if is_intersect():
                    return damnare_intersect(lower_block,upper_block)
                else:
                    return ['DAMNARE',area_lower+area_upper]
        else:#no intersect for x axis
            return ['DAMNARE',area_lower+area_upper]
    else:
        if is_intersect(lower_block,upper_block,y_ranges):
            return damnare_intersect(lower_block,upper_block)
        else:
            return ['DAMNARE',area_lower+area_upper]












        #[x1,y1,x2,y2]
    #[0,1,2,3]
