import mapnik
m = mapnik.Map(600,300)
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
s.rules.append(r)
m.append_style('Surya',s)
ds = mapnik.Shapefile(file="D:/Praktek/ne_110m_ocean.shx")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Surya')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'world.png','png')
print "rendered image to 'world.png"