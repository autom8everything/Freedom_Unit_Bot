
def csv2dict(filename):
    outdict = {}
    
    with open(filename) as f:
        headers = f.readline().strip().split(",")
        for key in headers:
            outdict[key] = []
            
        for line in f:
            line = line.strip().split(",")
            if len(line) == len(headers):
                for i,value in enumerate(line):
                    try:
                        outdict[headers[i]].append(float(value))
                    except:
                        outdict[headers[i]].append(value)
        
    return outdict
            
        