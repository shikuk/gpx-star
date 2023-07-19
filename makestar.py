#!/usr/bin/env python3
#coding=utf8

import gpxpy
import geopy
import geopy.distance
import argparse

parser = argparse.ArgumentParser(description='create gpx track as STAR')
parser.add_argument('-a', '--angle',  type=int, default=195, help='star slope in degrees, default 0 degree')
parser.add_argument('-d', '--distance',  type=int, default=150, help='star side length in meters, default 150 meters')
parser.add_argument('-s', '--start', type=float, nargs=2, metavar=('lat', 'lon'), required=True, help='First point of star, e.g. 56.31841 30.54227')
parser.add_argument('-o', '--out', type=str, default='/mnt/c/OziExplorer/Data/star-', help='Filename for track')
args = parser.parse_args()

firstA = args.angle
# 56.31841, 30.54227
lat, lon = args.start
start =  geopy.Point(lat, lon)
dist = args.distance
fname=args.out


addA = 216
points = [start]

print (points[0].format_decimal())
# Creating a new file:
# --------------------

gpx = gpxpy.gpx.GPX()

# Create first track in our GPX:
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Create first segment in our GPX track:
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

for i in range (6):
    p2 = geopy.distance.distance(meters=dist).destination(points[i], bearing=firstA + i*addA)
    print (p2.format_decimal())
    points.append([p2])
    gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(p2[0], p2[1], elevation=0))


print('Created GPX:', gpx.to_xml())
with open(fname + str(firstA) + ".gpx", "w") as f:
    f.write( gpx.to_xml())
