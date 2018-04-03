import mapnik
m = mapnik.Map(200,200)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#8f00ff')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('yellow'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Surya',s)
ds = mapnik.Shapefile(file="D:/Praktek4/ne_10m_minor_islands.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Surya')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'world.bmp','png')
print "rendered image to 'world.bmp"