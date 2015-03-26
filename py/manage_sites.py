import arcpy
import os
import numpy as np

arcpy.env.overwriteOutput = True

in_table = os.path.join(os.getcwd(), r'AllSitesTables.gdb/AllBDSites')
out_gdb = r"C:\temp\bdhsites.gdb"
field_names = ('OBJECTID', 'SITE_NAME', 'LAT', 'LONG', 'ZILLA', 'UPAZILLA', 'SITE_ID', 'SOURCE')

districts = set([row[0] for row in arcpy.da.SearchCursor(in_table, "ZILLA")])

for district in districts:
    
    if not district or district == '?????':
        continue
    expression = "ZILLA = {} AND Not (LONG = '' OR LONG = 'None')".format(district)
    table_view = "{}_view".format(district)
    arcpy.MakeTableView_management(in_table, table_view, expression)
    
    arr = arcpy.da.TableToNumPyArray(table_view, field_names)
    
    district_table = os.path.join(out_gdb, "{}_table".format(district)) #r'c:/data/TemplateData.gdb/{}_table'.format(district)
    district_points = os.path.join(out_gdb, "{}_points".format(district)) #r'c:/data/TemplateData.gdb/{}_points'.format(district)
    
    try:
        if arcpy.Exists(district_table):
            arcpy.Delete_management(district_table)
            
        arcpy.da.NumPyArrayToTable(arr, district_table)
        
        arcpy.ConvertCoordinateNotation_management(district_table, district_points, 'LONG', 'LAT', 'DMS_2', 'DD_NUMERIC')
    
        print('{} ..... done'.format(district))
    
    except Exception as ex:
        
        print(ex.args[0])