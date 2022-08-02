$(document).ready(function () {
    $('#example').DataTable({
        // Datatable configurations
        paging: true,
        pageLength: 5,
        lengthChange: true,
        autoWidth:true,
        searching:true,
        bInfo: true,
        bSort:true,
        language: {
            url: 'https://cdn.datatables.net/plug-ins/1.12.1/i18n/es-ES.json'
        }
    })
})