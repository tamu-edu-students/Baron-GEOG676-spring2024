import arcpy

# Assign Bands
source = r"C:\Users\ajbar\Desktop\GEOG_676\REP\Baron-GEOG676-spring2024\Labs\Lab07"
band01 = arcpy.sa.Raster(source + r"\Band01.tif") # Blue
band02 = arcpy.sa.Raster(source + r"\Band02.tif") # Green
band03 = arcpy.sa.Raster(source + r"\Band03.tif") # Red
band04 = arcpy.sa.Raster(source + r"\Band04.tif") # NIR
combined = arcpy.CompositeBands_management([band01, band02, band03, band04], source + r"\output_combined.tif")

# Hillshade
azimuth = 315
altitude = 45
shadows = 'NO_SHADOWS'
z_factor = 1
arcpy.ddd.HillShade(source + r"\DEM.tif", source +r"\output_Hillshade.tif", azimuth, altitude, shadows, z_factor)

# Slope
output_measurement = "DEGREE"
z_factor = 1
arcpy.ddd.Slope(source + r"\DEM.tif", source +r"\output_Slope.tif", output_measurement, z_factor)
print("Success!")