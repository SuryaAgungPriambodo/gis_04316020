import mapnik
m = mapnik.Map(1920,1080)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')

r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)

point_sym = mapnik.MarkersSymbolizer()
point_sym.filename

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[NAME]'), 'DejaVu Sans Bold',5,mapnik.Color('red'))
basinsLabels.halo_fill = mapnik.Color('yellow')
basinsLabels.halo_radius = 2
r.symbols.append(basinsLabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
r.symbols.append(point_sym)

s.rules.append(r)

m.append_style('Surya',s)
ds = mapnik.Shapefile(file="D:/Tugas 2/ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Surya')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('blue'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('Surya2',s)
ds = mapnik.Shapefile(file="D:/Tugas 2/INDONESIA_PROP.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Surya2')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('Surya3',s)
ds = mapnik.Shapefile(file="D:/Tugas 2/cina.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Surya3')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('black'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('Surya4',s)
ds = mapnik.Shapefile(file="D:/Tugas 2/mesir.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Surya4')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('Surya5',s)
ds = mapnik.Shapefile(file="D:/Tugas 2/prancis.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Surya5')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

point_sym = mapnik.MarkersSymbolizer()
point_sym.filename = 'D:/Tugas 2/gambar.png'
point_sym.width = mapnik.Expression("10")
point_sym.height = mapnik.Expression("10")
point_sym.allow_overlap = True
r.symbols.append(point_sym)

text_sym = mapnik.TextSymbolizer(mapnik.Expression('[Propinsi]'),'DejaVu Sans Bold',5,mapnik.Color('black'))
text_sym.halo_radius = 1
text_sym.allow_overlap = True
text_sym.avoid_edges = False
r.symbols.append(text_sym)

s.rules.append(r)
m.append_style('bonbin',s)

ds = mapnik.MemoryDatasource()
f = mapnik.Feature(mapnik.Context(),1)
f['Propinsi'] = 'Kebun Binatang Surabaya'
f.add_geometries_from_wkt("POINT(112.736111 -7.295833)")
ds.add_feature(f)

player = mapnik.Layer('bonbin_layer')
player.datasource = ds
player.styles.append('bonbin')
m.layers.append(player)

m.zoom_all()
mapnik.render_to_file(m,'world.pdf','pdf')
print "rendered image to 'world.pdf"