#!/usr/bin/python3

__author__='mleeds95'

import csv
import geojson

INFILE = 'UA_BARA_2014-08-18.csv'
OUTFILE = 'UA_BARA_2014-08-18.geojson'

def main():
    """Convert csv -> geojson."""
    allFeatures = []
    with open(INFILE) as f:
        reader = csv.DictReader(f)
        for row in reader:
            coords = row['Geocoding']
            if len(coords) > 0:
                point = geojson.Point((float(coords.split(',')[0]), float(coords.split(',')[1])))
                row.pop('Geocoding')
                feature = geojson.Feature(geometry=point, properties=row)
                allFeatures.append(feature)
    featureCollection = geojson.FeatureCollection(allFeatures)
    with open(OUTFILE, 'w') as f:
        geojson.dump(featureCollection, f)
    print('Wrote ' + str(len(allFeatures)) + ' places to ' + OUTFILE)

if __name__=='__main__':
    main()