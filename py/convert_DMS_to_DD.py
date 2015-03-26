import arcpy

fc = r'E:\BDArchaeology\DatabaseFinalStaging\AllSitesTables.gdb\AllBDSites'
#flds = arcpy.ListFields(fc)
#fnames = [f.name for f in flds if not f.required]
fnames = ('OBJECTID', 'SITE_NAME', 'DDLat', 'DDLon', 'ZILLA', 'UPAZILLA', 'SITE_ID', 'SOURCE')
rows = arcpy.da.SearchCursor(fc, fnames)

f = open(r'E:\BDArchaeology\DatabaseFinalStaging\allsites.txt', 'w')

for r in rows:
    f.writelines("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(r[0], r[1], r[2], r[3], r[4], r[5], 5[6]))
    
f.close()