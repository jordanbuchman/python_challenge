Python Challenge
=============

Installation
-----------

```
pip install -r requirements.txt
```

Usage
-----

```Python Challenge.

Usage:
  challenge <file> --outfile=<file> --format=<format> [--limit=<num>] [--filter=<rule> ...]
  challenge (-h | --help)
  challenge --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --outfile=<file>  Output filename.
  --format=<format>  Format of output. (json | xml | csv).
  --limit=<num>  Limit number of IPs processed.
  --filter=<rule> Specify filter rule. See help for details.

Filter Rules:
  in_radius(lat,long,radius): only output records within <radius> miles of <lat,long>.
  in_bbox(lat0,long0,lat1,long1): only output records within area bounded by <lat0,long0> at the upper right and <lat1,long1> at the bottom left.
  geoip_field_match(field,pattern): only output records with GeoIP field <field> equal to <pattern>.
  roles(role1,role2,...): only retrieve records with RDAP roles including <role1>, <role2>, ....
  only_roles(role1,role2,...): only include <role1>, <role2>, ... in records.
```
