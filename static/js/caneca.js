Highcharts.chart('container', {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Llenado de Caneca'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Plastico',
            y: 0,
            sliced: true,
            selected: true
        }, {
            name: 'Papel ',
            y: 0
        }, {
            name: 'Metal',
            y: 0
        }, {
            name: 'Vidrio',
            y: 0
        }, {
            name: 'Carton',
            y: 0
        }, {
            name: 'Basura',
            y: 0
        }]
    }]
});