#Create a GDB
import arcpy

arcpy.env.workspace = r'C:\Users\ajbar\Desktop\GEOG_676\REP\Baron-GEOG676-spring2024\Labs\Lab04\codes_env'
folder_path = r'C:\Users\ajbar\Desktop\GEOG_676\REP\Baron-GEOG676-spring2024\Labs\Lab04'
gdb_name = 'Lab04_AJB.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

#Create garage feature points
csv_path = r'C:\Users\ajbar\Desktop\GEOG_676\REP\Baron-GEOG676-spring2024\Labs\Lab04\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

#open campus gdb and copy building feature to provided gdb
campus = r'C:\Users\ajbar\Desktop\GEOG_676\REP\Baron-GEOG676-spring2024\Labs\Lab04\Campus.gdb'
building_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(building_campus, buildings)

#Reproject points
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_reprojected', spatial_ref)

#Buffer the Garages
garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + '\Garage_Points_buffered', 150)

#Intersect buffer with the buildings
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Building_intersection', 'ALL')

#I fought with this last portion of code for an hour and a half because I spelled "intersection" as "indersection...""
arcpy.TableToTable_conversion(gdb_path + '\Garage_Building_intersection.dbf', r'C:\Users\ajbar\Desktop\GEOG_676\REP\Baron-GEOG676-spring2024\Labs\Lab04', 'nearbyBuildings.csv')
