import mapnik
m = mapnik.Map(1920,1080)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')

r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('black'),1)
line_symbolizer.stroke_width = 0.5

r.symbols.append(line_symbolizer)

point_sym = mapnik.MarkersSymbolizer()
point_sym.filename

s.rules.append(r)

m.append_style('Surya',s)
ds = mapnik.Shapefile(file="D:/Tugas-7(CP1)/SuryaCP1/INDONESIA_PROP.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Surya')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[wisata]'),'DejaVu Sans Bold',3,mapnik.Color('red'))
basinsLabels.halo_fill = mapnik.Color('yellow')
basinsLabels.halo_radius = 1
r.symbols.append(basinsLabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
point_sym.opacity = 0.5
point_sym.file = () 
r.symbols.append(point_sym)

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'),1)
r.symbols.append(line_symbolizer)
point = mapnik.PointSymbolizer()
r.symbols.append(point)
s.rules.append(r)

m.append_style('Surya2',s)
POSTGIS_TABLE = dict(
 	host='localhost',
 	port=5432,
 	user='postgres',
 	password='54719000',
 	dbname='kelasgis',
 	table='(select ST_Buffer(ST_Centroid(geom),1) as geom, wisata from surya) as coba',
)
ds = mapnik.PostGIS(**POSTGIS_TABLE)
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Surya2')
m.layers.append(layer)

m.zoom_all()
mapnik.render_to_file(m,'Indonesia.jpeg','jpeg')
print "rendered image to 'Indonesia.jpeg"