
import arcpy, os

arcpy.env.workspace = r'D:\Personal\_blog\_importKML\_data\_kmz'
outLocation = r'D:\Personal\_blog\_importKML\_data\_gdb'
MasterGDB = 'AllKMLLayers.gdb'
MasterGDBLocation = os.path.join(outLocation, MasterGDB)

print 'Master'

for kmz in arcpy.ListFiles('*.KM*'):
  print ("CONVERTING: {0}".format(os.path.join(arcpy.env.workspace, kmz)))
  arcpy.KMLToLayer_conversion(kmz, outLocation)

arcpy.env.workspace = outLocation
wks = arcpy.ListWorkspaces('*', 'FileGDB')
wks.remove(MasterGDBLocation)

for fdgb in wks:

	arcpy.env.workspace = fdgb
	featureClasses = arcpy.ListFeatureClasses('*', '', 'Placemarks')
	
	for fc in featureClasses:
		print ("COPYING: {0} FROM: {1}".format(fc, fgdb))    
		fcCopy = os.path.join(fgdb, 'Placemarks', fc)
		arcpy.FeatureClassToFeatureClass_conversion(fcCopy, MasterGDBLocation, fgdb[fgdb.rfind(os.sep)+1:-4])
  

# Clean up
del kmz, wks, fc, featureClasses, fgdb  