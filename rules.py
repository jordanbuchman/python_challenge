import re

def rules_applier(rules,records):
  for rule in rules:
    name, args = rules_parser(rule)
    rule_list = {
      'in_bbox': lambda record: record.in_bbox((float(args[0]),float(args[1])),(float(args[2]),float(args[3]))),
      'in_radius': lambda record: record.in_radius((float(args[0]),float(args[1])),float(args[2])),
      'geoip_field_match': lambda record: record.field_match(*args),
      'roles': lambda record: record.check_roles(args),
      'only_roles': lambda record: record.only_roles(args)
    }
    if name in rule_list:
      records = list(filter(rule_list[name], records))
  return records

def rules_parser(rule):
  parts = re.search(r'(.+)\((.+)\)',rule).groups()
  name = parts[0]
  args = parts[1].split(',')
  return name, args

