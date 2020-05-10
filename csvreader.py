
def csv2dict(filename):
    outdict = {}
    
    with open(filename) as f:
        headers = f.readline().strip().split(",")
        for key in headers:
            outdict[key] = []
            
        c = 0
        for line in f:
            c += 1
            if c > 1: #skip header
                line = f.readline().strip().split(",")
                for i,value in enumerate(line):
                    try:
                        outdict[headers[i]].append(float(value))
                    except:
                        outdict[headers[i]].append(value)
        
    return outdict
            
        