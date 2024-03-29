
Map {
  background-color: #fff;
}

#markers {
  marker-width:26.66;
  marker-line-width:6.4;
  marker-fill:#000;
  marker-line-color:#fff;
  marker-opacity:1;
  marker-allow-overlap:true;
  text-name: [featureName];
  text-face-name: 'Avenir Heavy';
  text-size: 44.440;
  text-fill: #000;
  text-halo-radius: 6.400;
  text-halo-fill: #fff;
  text-dx: 13.330;
  text-dy: 22.220;
  text-placement-type: simple;
  text-placements: S;
  text-opacity:1;
}

#boulderGNIS::markers {
  marker-width:26.66;
  marker-line-width:6.4;
  marker-fill:#000;
  marker-line-color:#fff;
  marker-opacity:1;
  marker-allow-overlap:true;
}

#boulderGNIS::labels {
  text-name: [featureName];
  text-face-name: 'Avenir Heavy';
  text-size: 44.440;
  text-fill: #000;
  text-halo-radius: 6.400;
  text-halo-fill: #fff;
  text-dx: 13.330;
  text-dy: 22.220;
  text-placement-type: simple;
  text-placements: N,S,E,W,NE,SE,NW,SW;
  text-opacity:1;
  [featureClass='Summit'] {
    text-name: [featureName] + ' (' + [elevationFeet] + ')';
  }
  [featureName='KBCO-AM (Boulder)'],
    [featureName='Mount Epworth'][elevationFeet=11847] {
    text-placements: "SE";
  }
  [featureName='Haystack Mountain'],
    [featureName='Table Mountain'][elevationFeet=5620] {
    text-placements: "NE";
  }
  [featureName='Devils Thumb'],
    [featureName='Table Mountain'][elevationFeet=6204],
    [featureName='Poorman Hill'],
    [featureName='Shanahan Hill'] {
    text-placements: "SW";
  }
}


.contour {
  
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
  {
    line-width: 4.950;
    line-join: round;
    line-cap: round;
    line-color: #178;
    line-opacity: 0.600;
  }
  
  ::major {
    [CONTOURELE=5000],[CONTOURELE=6000],[CONTOURELE=7000],[CONTOURELE=8000],
    [CONTOURELE=9000],[CONTOURELE=10000],[CONTOURELE=11000],[CONTOURELE=12000],
    [CONTOURELE=13000],[CONTOURELE=14000],[CONTOURELE=15000]
    {
      line-width: 8.000;
      line-join: round;
      line-cap: round;
      line-color: #178;
      line-opacity: 1.000;
      text-name: "[CONTOURELE].replace('0\.0','0')";
      text-face-name: 'Avenir Heavy';
      text-size: 44.440;
      text-fill: #178;
      text-halo-radius: 6.400;
      text-halo-fill: #fff;
      text-placement: line;
      text-opacity:1;
    }
  }
    
}

#majorRoads {
  ::case {
    line-width: 8.010;
    line-join: round;
    line-cap: round;
    line-color: #fff;
    line-opacity: 1.000;
    [CLASS='Federal'] {
      line-width: 12.950;
      line-join: round;
      line-cap: round;
      line-color: #fff;
      line-opacity: 1.000;
    }
  }
  ::fill {
    line-width: 4.950;
    line-join: round;
    line-cap: round;
    line-color: #000;
    line-opacity: 1.000;
    [CLASS='Federal'] {
      line-width: 8.000;
      line-join: round;
      line-cap: round;
      line-color: #000;
      line-opacity: 1.000;
    }
  }
  [CLASS='Federal'] {
    text-name: 'US ' + [NUMBER];
    text-face-name: 'Avenir Heavy';
    text-size: 44.440;
    text-fill: #000;
    text-halo-radius: 6.400;
    text-halo-fill: #fff;
    text-placement: line;
    text-opacity:1;
  }
}

#graticule {
  line-width: 4.950;
  line-join: round;
  line-cap: round;
  line-color: #a55;
  line-opacity: 0.800;
  text-name: [name];
  text-face-name: 'Avenir Heavy';
  text-size: 44.440;
  text-fill: #811;
  text-halo-radius: 6.400;
  text-halo-fill: #fff;
  text-placement: line;
  text-opacity:1;
}

