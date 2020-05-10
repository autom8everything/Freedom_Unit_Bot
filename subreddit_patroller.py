import re, praw

#patrolling incoming comments for requests or units
def patrol(bot,units,targetsub,keyphrase,patrol_sub,frequency):
    
    #looping through all incoming comments
    for comment in bot.subreddit(targetsub).stream.comments(skip_existing=True):
        
        if keyphrase in comment.body:
            hasconversion,reply_string = check_comment(comment.body,units)
            #comment.reply(reply_string)
            print(f"Would have replied with:\n{reply_string}")
            


#checking comment for units or abbreviations, returning reply
def check_comment(comment,units):
    
    #check using full unit names
    hasconversion,reply_string = check_for_units(comment,units,"units")
    
    #check using abbreviations
    if not hasconversion:
        hasconversion,reply_string = check_for_units(comment,units,"abbreviation")
    
    return hasconversion,reply_string
    


#checking comment for each unit type, returning reply    
def check_for_units(comment,units,key):
    #try full wording for units
    for i,unit_to_check in enumerate(units[key]):
        hasunits,unitvalue = parse_for_values(comment,unit_to_check)
        
        if hasunits: #if an expression with listed units and a number are found
            newunits = units["freedomunits"][i]
            newvalue = unitvalue*units["conversionfactor"][i]
            
            #creating reply
            reply_string = f"{unitvalue} {unit_to_check} is {newvalue} {newunits}"
            return True, reply_string
            
    #if no units could be found
    return False,"I was unable to find anything to convert in this comment :("
            
    
    
#checking comment for units and value            
def parse_for_values(comment,unit):
    if unit in comment:
        match = re.search(rf"[\d.-]* {unit}",comment) #regexp to search for units
        try:
            unitvalue = float(match.group(0)[:-len(unit)-1])
            return True,unitvalue
        except:
            pass
    
    #if not found
    return False,0

