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
    })
})