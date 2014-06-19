"""
A script to fix the CONTOURELE field of USGS elevation shapefiles so that
elevation labels in TileMill won't all have a useless ".0" at the end.

This depends on Pyshp: https://github.com/GeospatialPython/pyshp
"""

import shapefile

denver = shapefile.Reader("denverElevation/Elev_Contour")
print "Denver has {} shapes and {} records with the following fields:\n\n {}".format(
	len(denver.shapes()),
	len(denver.records()),
	denver.fields
	)

print
print

greeley = shapefile.Reader("greeleyElevation/Elev_Contour")
print "Greeley has {} shapes and {} records with the following fields:\n\n {}".format(
	len(greeley.shapes()),
	len(greeley.records()),
	greeley.fields
	)

"""
TODO
1. for each shapefile...
2. for each shape/record pair...
2. copy the shape as-is to a new shapefile
3. filter the record to the new shapefile, discarding all fields but CONTOURELE,
   and changing its type from N (long integer?) to C (character), making sure the
   character string is formatted as an integer with no ".0" at the end!
"""
