import arcpy

fc = r'E:\BDArchaeology\DatabaseFinalStaging\AllSitesTables.gdb\AllBDSites'
#flds = arcpy.ListFields(fc)
#fnames = [f.name for f in flds if not f.required]
fnames = ('OBJECTID', 'SITE_NAME', 'DDLat', 'DDLon', 'ZILLA', 'UPAZILLA', 'SITE_ID', 'SOURCE')
rows = arcpy.da.SearchCursor(fc, fnames)

f = open(r'E:\BDArchaeology\DatabaseFinalStaging\allsites.txt', 'w')

for r in rows:
    oid = r[0]
    #print(type(oid))
    sitename = r[1]
    #print(type(sitename))
    ddlat = r[2]
    #print(type(ddlat))
    ddlon = r[3]
    #print(type(ddlon))
    zilla = r[4]
    #print(type(zilla))
    uzilla = r[5]
    #print(type(zilla))
    siteid = r[6]
    #print(type(siteid))
    source = r[7]
    #print(type(source))
    f.writelines("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(oid, sitename, ddlat, ddlon, zilla, uzilla, siteid, source))
    
f.close()
