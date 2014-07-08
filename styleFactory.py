# =========================================================================================================
# Calculate the scaling factor to apply to sizes and line widths. At the moment the scaling factor is 1.0
# because the starting sizes and line widths were pre-calculated in a spreadsheet. This is nearly
# equivalent to what the scale factor slider does, except this method allows the scale factor to be set
# with more precision.
# =========================================================================================================
inputDPI = 600.0
outputDPI = 600.0
scale = outputDPI / inputDPI


# =========================================================================================================
# These functions create blocks of CartoCSS according to the specified  colors, line widths, font sizes,
# and opacities. Widths and sizes are scaled by the scaling factor calculated above.
# =========================================================================================================
def lineStyle(width,color,opacity=1.0,indent="  "):
  return ("line-width: {:.3f};\n"
          "{indent}line-join: round;\n"
          "{indent}line-cap: round;\n"
          "{indent}line-color: {};\n"
          "{indent}line-opacity: {:.3f};").format(width*scale,color,opacity,indent=indent)

def markersStyle(width=26.66,lineWidth=6.4,indent="  "):
  return ("marker-width:{};\n"
      "{indent}marker-line-width:{};\n"
      "{indent}marker-fill:#000;\n"
      "{indent}marker-line-color:#fff;\n"
      "{indent}marker-opacity:1;\n"
      "{indent}marker-allow-overlap:true;").format(width*scale,lineWidth*scale,indent=indent)

def textStyle(name,fill="#000",size=44.44,dx=13.33,dy=22.22,haloRadius=6.4,
    placement="",placementType="simple",placements="N,S,E,W,NE,SE,NW,SW",indent="  ",isLine=False):

  if placement == "":
    # If line placement wasn't specified, then use point placement
    placement = ("text-placement-type: {};\n"
           "{indent}text-placements: {};").format(placementType,placements,indent=indent)
  elif placement == "line":
    placement = "text-placement: line;"

  if isLine:
      dxDy = ""
  else:
    dxDy = ("{indent}text-dx: {:.3f};\n"
          "{indent}text-dy: {:.3f};\n").format(dx*scale,dy*scale,indent=indent)

  return ("text-name: {};\n"
      "{indent}text-face-name: 'Avenir Heavy';\n"
      "{indent}text-size: {:.3f};\n"
      "{indent}text-fill: {};\n"
      "{indent}text-halo-radius: {:.3f};\n"
      "{indent}text-halo-fill: #fff;\n"
      "{dxDy}"
      "{indent}{}\n"
      "{indent}text-opacity:1;"
      ).format(name,size*scale,fill,haloRadius*scale,placement,dxDy=dxDy,indent=indent)


# =========================================================================================================
# The parameters to these function calls make up a compressed specification of the style. The point is
# to make it easier to set colors consistently, and to ajust relative sizes and widths, without having
# to scroll through a lot of CartoCSS
# =========================================================================================================
markers = markersStyle()

markersText      = textStyle(name="[featureName]",placements="S")
gnisText         = textStyle(name="[featureName]")
majorContourText = textStyle(name="\"[CONTOURELE].replace('0\.0','0')\"",
                             fill="#178",placement="line",indent="      ",isLine=True)
federalText      = textStyle(name="'US ' + [NUMBER]",fill="#000",placement="line",indent="    ",isLine=True)
graticuleText    = textStyle(name='[name]',          fill="#811",placement="line",isLine=True)

minorContour = lineStyle(width= 4.95,color="#178",opacity=0.6,indent="    ")
majorContour = lineStyle(width= 8.00,color="#178",indent="      ")
stateCase    = lineStyle(width= 8.01,color="#fff",indent="    ")
federalCase  = lineStyle(width=12.95,color="#fff",indent="      ")
stateFill    = lineStyle(width= 4.95,color="#000",indent="    ")
federalFill  = lineStyle(width= 8.00,color="#000",indent="      ")
graticule    = lineStyle(width= 4.95,color="#a55",opacity=0.8)


# =========================================================================================================
# This long format string contains portions of the map's CartoCSS style which are not sensitive to scaling,
# along with named variables for the blocks of CartoCSS calculated by the functions above.
# =========================================================================================================
print """
Map {{
  background-color: #fff;
}}

#markers {{
  {markers}
  {markersText}
}}

#boulderGNIS::markers {{
  {markers}
}}

#boulderGNIS::labels {{
  {gnisText}
  [featureClass='Summit'] {{
    text-name: [featureName] + ' (' + [elevationFeet] + ')';
  }}
  [featureName='KBCO-AM (Boulder)'],
    [featureName='Mount Epworth'][elevationFeet=11847] {{
    text-placements: "SE";
  }}
  [featureName='Haystack Mountain'],
    [featureName='Table Mountain'][elevationFeet=5620] {{
    text-placements: "NE";
  }}
  [featureName='Devils Thumb'],
    [featureName='Table Mountain'][elevationFeet=6204],
    [featureName='Poorman Hill'],
    [featureName='Shanahan Hill'] {{
    text-placements: "SW";
  }}
}}


.contour {{
  
  [CONTOURELE=4680],[CONTOURELE=4720],[CONTOURELE=4760],[CONTOURELE=4800],[CONTOURELE=4840],
  [CONTOURELE=4880],[CONTOURELE=4920],[CONTOURELE=4960],[CONTOURELE=5080],[CONTOURELE=5120],
  [CONTOURELE=5200],[CONTOURELE=5280],[CONTOURELE=5360],[CONTOURELE=5440],[CONTOURELE=5520],
  [CONTOURELE=5600],[CONTOURELE=5680],[CONTOURELE=5760],[CONTOURELE=5840],[CONTOURELE=5920],
  [CONTOURELE=6080],[CONTOURELE=6120],[CONTOURELE=6200],[CONTOURELE=6280],
  [CONTOURELE=6360],[CONTOURELE=6440],[CONTOURELE=6520],[CONTOURELE=6600],
  [CONTOURELE=6680],[CONTOURELE=6760],[CONTOURELE=6840],[CONTOURELE=6920],
  [CONTOURELE=7080],[CONTOURELE=7120],[CONTOURELE=7200],[CONTOURELE=7280],
  [CONTOURELE=7360],[CONTOURELE=7440],[CONTOURELE=7520],[CONTOURELE=7600],
  [CONTOURELE=7680],[CONTOURELE=7760],[CONTOURELE=7840],[CONTOURELE=7920],
  [CONTOURELE=8080],[CONTOURELE=8120],[CONTOURELE=8200],[CONTOURELE=8280],
  [CONTOURELE=8360],[CONTOURELE=8440],[CONTOURELE=8520],[CONTOURELE=8600],
  [CONTOURELE=8680],[CONTOURELE=8760],[CONTOURELE=8840],[CONTOURELE=8920],
  [CONTOURELE=9080],[CONTOURELE=9120],[CONTOURELE=9200],[CONTOURELE=9280],
  [CONTOURELE=9360],[CONTOURELE=9440],[CONTOURELE=9520],[CONTOURELE=9600],
  [CONTOURELE=9680],[CONTOURELE=9760],[CONTOURELE=9840],[CONTOURELE=9920],
  [CONTOURELE=10080],[CONTOURELE=10120],[CONTOURELE=10200],[CONTOURELE=10280],
  [CONTOURELE=10360],[CONTOURELE=10440],[CONTOURELE=10520],[CONTOURELE=10600],
  [CONTOURELE=10680],[CONTOURELE=10760],[CONTOURELE=10840],[CONTOURELE=10920],
  [CONTOURELE=11080],[CONTOURELE=11120],[CONTOURELE=11200],[CONTOURELE=11280],
  [CONTOURELE=11360],[CONTOURELE=11440],[CONTOURELE=11520],[CONTOURELE=11600],
  [CONTOURELE=11680],[CONTOURELE=11760],[CONTOURELE=11840],[CONTOURELE=11920],
  [CONTOURELE=12080],[CONTOURELE=12120],[CONTOURELE=12200],[CONTOURELE=12280],
  [CONTOURELE=12360],[CONTOURELE=12440],[CONTOURELE=12520],[CONTOURELE=12600],
  [CONTOURELE=12680],[CONTOURELE=12760],[CONTOURELE=12840],[CONTOURELE=12920],
  [CONTOURELE=13080],[CONTOURELE=13120],[CONTOURELE=13200],[CONTOURELE=13280],
  [CONTOURELE=13360],[CONTOURELE=13440],[CONTOURELE=13520],[CONTOURELE=13600],
  [CONTOURELE=13680],[CONTOURELE=13760],[CONTOURELE=13840],[CONTOURELE=13920],
  [CONTOURELE=14080],[CONTOURELE=14120],[CONTOURELE=14200],[CONTOURELE=14280],
  [CONTOURELE=14360],[CONTOURELE=14440],[CONTOURELE=14520],[CONTOURELE=14600],
  [CONTOURELE=14680],[CONTOURELE=14760],[CONTOURELE=14840],[CONTOURELE=14920]
  {{
    {minorContour}
  }}
  
  ::major {{
    [CONTOURELE=5000],[CONTOURELE=6000],[CONTOURELE=7000],[CONTOURELE=8000],
    [CONTOURELE=9000],[CONTOURELE=10000],[CONTOURELE=11000],[CONTOURELE=12000],
    [CONTOURELE=13000],[CONTOURELE=14000],[CONTOURELE=15000]
    {{
      {majorContour}
      {majorContourText}
    }}
  }}
    
}}

#majorRoads {{
  ::case {{
    {stateCase}
    [CLASS='Federal'] {{
      {federalCase}
    }}
  }}
  ::fill {{
    {stateFill}
    [CLASS='Federal'] {{
      {federalFill}
    }}
  }}
  [CLASS='Federal'] {{
    {federalText}
  }}
}}

#graticule {{
  {graticule}
  {graticuleText}
}}
""".format(markersText=markersText,markers=markers,gnisText=gnisText,
       minorContour=minorContour,majorContour=majorContour,
       majorContourText=majorContourText,stateCase=stateCase,
       federalCase=federalCase,stateFill=stateFill,federalFill=federalFill,
       federalText=federalText,graticule=graticule,graticuleText=graticuleText)
