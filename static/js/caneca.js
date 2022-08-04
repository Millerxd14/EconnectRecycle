// Highcharts.chart('container', {
//     chart: {
//         plotBackgroundColor: null,
//         plotBorderWidth: null,
//         plotShadow: false,
//         type: 'pie'
//     },
//     title: {
//         text: 'Llenado de Caneca'
//     },
//     tooltip: {
//         pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
//     },
//     accessibility: {
//         point: {
//             valueSuffix: '%'
//         }
//     },
//     plotOptions: {
//         pie: {
//             allowPointSelect: true,
//             cursor: 'pointer',
//             dataLabels: {
//                 enabled: true,
//                 format: '<b>{point.name}</b>: {point.percentage:.1f} %'
//             }
//         }
//     },
//     series: [{
//         name: 'Brands',
//         colorByPoint: true,
//         data: [{
//             name: 'Plastico',
//             y: 0,
//             sliced: true,
//             selected: true
//         }, {
//             name: 'Papel ',
//             y: 0
//         }, {
//             name: 'Metal',
//             y: 0
//         }, {
//             name: 'Vidrio',
//             y: 0
//         }, {
//             name: 'Carton',
//             y: 0
//         }, {
//             name: 'Basura',
//             y: 0
//         }]
//     }]
// });

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