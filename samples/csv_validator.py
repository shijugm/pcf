



#json_schema = {"dec1": ['isnull'], "dec2": ['decimal'], "dec3": ['decimal'], "dec4": ['decimal'], "dec5": ['decimal'], "dec6": ['decimal'], "dec7": ['decimal'], "company_id": ['int', 'null'], "currency_id": ['int', 'null'], "country_id": ['int', 'null'] }
json_schema = {"dec1": ['isnull'], "dec2": ['decimal'], "dec3": ['decimal'], }

def isnull(val):
    return val is None

def decimal(val):
    return val is None

def do_validation():
    # read the data
    for k, vals in json_schema.items():
        print (k , vals)
        print(vals[0] + "(1)")
        print (eval(vals[0]+ "(1)"))



if __name__ == '__main__':
    do_validation()