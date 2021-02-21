
# #input is a list of dict
# import json
# import re
# class BusCompany():
#     #first key stores the type, second whether the boolean is required or not and third stores whether the number of errors
#     required_field_types = {
#         "bus_id": {"type":int,"required":True},
#         "stop_id": {"type":int,"required":True},
#         "stop_name": {"type":str,"required":True,"format":re.compile(r"^([A-Z][a-z]+ )+(Road|Avenue|Boulevard|Street)$")},
#         "next_stop": {"type":int,"required":True},
#         "stop_type": {"type": "char","required":False,"format":re.compile(r"^[SOF]?$")},
#         "a_time": {"type":str,"required":True,"format": re.compile(r"^([01]\d|2[0-3]):[0-5]\d$")}
#                             }
#     #creating dict for updating errors
#     errors = dict.fromkeys(required_field_types,0)
#
#     def __init__(self,dict_data):
#         self.dict_data = dict_data
#         self.dict_data = json.loads(self.dict_data)
#         #this is a list of dicts
#
#     def validate(self):
#         for dict_elem in self.dict_data:
#             for k, v in dict_elem.items():
#                 #check if value is empty and it was required at the first place
#                 if (v =="" and BusCompany.required_field_types[k]["required"]==True) :
#                     BusCompany.errors[k]+=1
#                 #value is not empty, now check for correct type of data i,e Type error
#                 else:
#                     #check if the types are not equal
#                     if (type(v)!=BusCompany.required_field_types[k]["type"]):
#                         #if the type is not equal to char
#                         if BusCompany.required_field_types[k]["type"]!="char":
#                             BusCompany.errors[k]+=1
#                         else:
#                             #check if type(v) is a string and other being char i.e length 1 string
#                             if type(v)!=str:
#                                 #check if this is string of len1 then only char else
#                                 BusCompany.errors[k]+=1
#                             elif len(v)>1:
#                                 BusCompany.errors[k]+=1
#                             #if everything is valid then check for format error
#                             #else:
#                             #    format_val = BusCompany.required_field_types[k].get("format")
#                             #    if format_val:
#                             #        if re.match(format_val,v)==None:
#                             #            BusCompany.errors[k]+=1
#
#         sum_errors = sum([elem for elem in BusCompany.errors.values()])
#
#         return BusCompany.errors,sum_errors
#
#     #method to print out the output
#     def display_output(self):
#         out_dict,error_sum = self.validate()
#         print("Type and required fields validation: {} errors".format(error_sum))
#         for k,v in out_dict.items():
#             print("{}: {}".format(k,v))
#
#     #@staticmethod
#     #bound to just class not the object
#
# input_dict = input()
# bus_company = BusCompany(input_dict)
# bus_company.display_output()
## Stage 1 solution ends here..
# Stage 2 solution starts here

# Write your awesome code here
#input is a list of dict
# import json
# import re
# class BusCompany():
#     #first key stores the type, second whether the boolean is required or not and third stores whether the number of errors
#     required_field_types = {
#         "bus_id": {"type":int,"required":True},
#         "stop_id": {"type":int,"required":True},
#         "stop_name": {"type":str,"required":True,"format":re.compile(r"^([A-Z][a-z]+ )+(Road|Avenue|Boulevard|Street)$")},
#         "next_stop": {"type":int,"required":True},
#         "stop_type": {"type": "char","required":False,"format":re.compile(r"^[SOF]?$")},
#         "a_time": {"type":str,"required":True,"format": re.compile(r"^([01]\d|2[0-3]):[0-5]\d$")}
#                             }
#     #creating dict for updating errors
#     errors = dict.fromkeys(required_field_types,0)
#
#     def __init__(self,dict_data):
#         self.dict_data = dict_data
#         self.dict_data = json.loads(self.dict_data)
#         #this is a list of dicts
#
#     def validate(self):
#         for dict_elem in self.dict_data:
#             for k, v in dict_elem.items():
#                 format_val = BusCompany.required_field_types[k].get("format")
#                 if format_val and re.match(format_val,v)==None:
#                         BusCompany.errors[k]+=1
#
#         sum_errors = sum([elem for elem in BusCompany.errors.values()])
#
#         return BusCompany.errors,sum_errors
#
#     #method to print out the output
#     def display_output(self):
#         out_dict,error_sum = self.validate()
#         print("Format validation: {} errors".format(error_sum))
#         for k,v in out_dict.items():
#             if v!=0:
#                 print("{}: {}".format(k,v))
#
#     #@staticmethod
#     #bound to just class not the object
#
# input_dict = input()
# bus_company = BusCompany(input_dict)
# bus_company.display_output()

# Stage 2 solution ends here

## Stage 3 solution starts here
# import json
# json_data = json.loads(input())
# busstops = {}
# for data in json_data:

#     # initialising the value of the dict to be an empty list
#     busstops.setdefault(data["bus_id"], [])
#     #now add the data
#     busstops[data["bus_id"]].append(data["stop_id"])
#
# print("Line names and number of stops:")
# for k,v in busstops.items():
#     print("bus_id: {0}, stops: {1}".format(k,len(v)))

#Stage 4 solution
# import json
#
# json_data = json.loads(input())
# register = {}
# for data in json_data:
#     #initialising the value of dict to be an empty list for each bus id
#     register.setdefault(data["bus_id"], [])
#     #appending
#     register[data["bus_id"]].append(data)
#
# for k, v in register.items():
#     start, end = 0, 0
#     for e in v:
#         if e["stop_type"] == "S":
#             start += 1
#         elif e["stop_type"] == "F":
#             end += 1
#     if start != 1 or end != 1:
#         print("There is no start or end stop for the line: {}.".format(k))
#         break
#
# total_stops, start, mid, end = [], [], [], []
# for data in json_data:
#     total_stops.append(data["stop_name"])
#     if data["stop_type"] == "S":
#         start.append(data["stop_name"])
#     elif data["stop_type"] == "F":
#         end.append(data["stop_name"])
# #finding out unique stops and appending
# for stop in set(total_stops):
#     if total_stops.count(stop) > 1:
#         mid.append(stop)
#
# mid.sort()
# start = sorted(set(start))
# end = sorted(set(end))
#
# print("Start stops:", len(start), start)
# print("Transfer stops:", len(mid), mid)
# print("Finish stops:", len(end), end)
# Stage 4 ends here


# Stage 5 solution
# import json
#
# json_data = json.loads(input())
# register = {}
# for data in json_data:
#     #initialising the value of dict to be an empty list for each bus id
#     register.setdefault(data["bus_id"], [])
#     #appending
#     register[data["bus_id"]].append(data)
#
# print("Arrival time test:")
# flag = True
# for k, v in register.items():
#     arrival_time = v[0]["a_time"]
#     for e in v[1:]:
#         if arrival_time > e["a_time"]:
#             print("bus_id line", k, ": wrong time on station", e["stop_name"])
#             flag = False
#             break
#         arrival_time = e["a_time"]
# if flag:
#     print("OK")
#
# Stage 5 solution ends here

# Stage 6: Final stage solution
import json
import itertools

json_data = json.loads(input())
register = {}
for data in json_data:
    #initialising the value of dict to be an empty list for each bus id
    register.setdefault(data["stop_type"], [])
    #appending
    register[data["stop_type"]].append(data["stop_name"])

    mid = []
    for name in set(itertools.chain(*register.values())):
        if list(itertools.chain(*register.values())).count(name) > 1:
            mid.append(name)

    print("On demand stops test:")
    out = set(register.get("O", [])) & set(itertools.chain(register.get("S", []),register.get("F", []),register.get("", []),mid,))
    print("Wrong stop type:", sorted(out)) if out else print("OK")
