Highcharts.chart('container', {
  chart: {
      type: 'column'
  },
  title: {
      align: 'left',
      text: 'Llenado de Caneca'
  },
  xAxis: {
      title: {
          text: 'Productos'
      },
      categories:['Plastico', 'Papel', 'Metal', 'Vidrio', 'Carton', 'Basura']
  },
  yAxis: {
      title: {
          text: 'porcentaje de llenado'
      }

  },
  legend: {
      enabled: false
  },
  plotOptions: {
      series: {
          borderWidth: 0,
          dataLabels: {
              enabled: true,
              format: '{point.y:.2f}%'
          }
      }
  },

  series: [
      {
          name: "Caneca",
          data: [
              {
                  name: "Plastico",
                  color: '#0E22B6',
                  y: 62.74,
                  drilldown: "Plastico"
              },
              {
                  name: "Papel",
                  color:'#BDBDBD',
                  y: 10.57,
                  drilldown: "Papel"
              },
              {
                  name: "Metal",
                  color:'#FBFF1F',
                  y: 7.23,
                  drilldown: "Metal"
              },
              {
                  name: "Vidrio",
                  color:'#40FFE6',
                  y: 5.58,
                  drilldown: "Vidrio"
              },
              {
                  name: "Carton",
                  color:'#FF641F',
                  y: 4.02,
                  drilldown: "Carton"
              },
              {
                  name: "Basura",
                  color:'#418A36',
                  y: 1.92,
                  drilldown: "Basura"
              },
          ]
      }
  ],
});
Highcharts.chart('container', {
    chart: {
      type: 'column'
    },
    title: {
      text: 'Porcentaje de llenado de canecas'
    },
    xAxis: {
      categories: [
        'Plástico',
        'Papel',
        'Metal',
        'Vidrio',
        'Carton',
        'Basura'
      ],
      crosshair: true
    },
    tooltip: {
        pointFormat: '<tr><td style="color:#000;padding:0"> {point.y:.1f} %</td>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
      },
    colors: [
        '#0E22B6', 
        '#BDBDBD', 
        '#FBFF1F', 
        '#40FFE6', 
        '#FF641F', 
        '#418A36'
    ],
    yAxis: {
      min: 0,
      title: {
        text: '%'
      }
    },
    plotOptions: {
      column: {
        pointPadding: 0.2,
        borderWidth: 0,
        colorByPoint: true
      }
    },
    series: [{
      name: 'Caneca',
      data: _values
  
    }]
  });