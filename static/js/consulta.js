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
function aceptar_recolector(id){

  completa_url = '/users/aceptar_recolector/'+id;
  $.ajax({
    type: "GET",
    url: completa_url,
    data: id= id,
      success: function(data)
      {
        send_notification( data['tipo'],data['titulo'],data['mensaje'],'3000');
        $('#aceptar'+id).hide();
      }
  });
}

function aceptar_productor(id){

  completa_url = '/users/aceptar_productor/'+id;
  $.ajax({
    type: "GET",
    url: completa_url,
    data: id= id,
      success: function(data)
      {
        send_notification( data['tipo'],data['titulo'],data['mensaje'],'3000');
        $('#aceptar'+id).hide();
      }
  });
}


function rechazar_visualizacion(tipo, id){
  completa_url = '/users/rechazar_visualizacion/'+tipo+'/'+id;
  $.ajax({
    type: "GET",
    url: completa_url,
    data: id= id,
      success: function(data)
      {
        send_notification( data['tipo'],data['titulo'],data['mensaje'],'3000');
        setTimeout("location.reload(true);", 1000);
      }
  });
}



function datos_usuario(id){
  completa_url = '/users/datos_usuario/'+id;
  $.ajax({
    type: "GET",
    url: completa_url,
    data: id= id,
      success: function(data)
      { 
        contenido = '<p>'+ data['telefono_productor']+'</p>'+ '<p>'+ data['correo_productor']+'</p>';
        $('#contenido_datos_usuarios').html(contenido);
        $('#modal_datos_usuario').modal('show');
      }
  });
}




function buscar_canecas(id_usuario, nombre_usuario){
  completa_url = '/caneca/buscar_canecas/'+id_usuario;
  $.ajax({
    type: "GET",
    url: completa_url,
    data: id_usuario= id_usuario,
      success: function(data)
      {
        $('#titulo_modal').html('Canecas de ' + nombre_usuario);
        if( Object.keys(data).length == 0 ){
          $('#conenido_modal').html('Este usuario no tiene canecas disponibles');
        }else{
          contenido = "<table class='table  table-bordered table-responsive caption-top'>" +
          "<thead class='table-otro'>"+
              "<th class='text-center' >Nombre</th>"+
              "<th class='text-center' >Descripción</th>"+
              "<th class='text-center' >Plástico</th>"+
              "<th class='text-center' >Vidrio</th>"+
              "<th class='text-center' >Cartón</th>"+
              "<th class='text-center' >Metal</th>"+
              "<th class='text-center' >Organico</th>"+
              "<th class='text-center' >Papel</th>"+
          "</thead>"+
          "<tbody>"
          ;
          for (const object in data) {
            contenido = contenido +
              "<tr>"+
                "<td class='text-center' >"+data[object]['name']+"</td>"+
                "<td class='text-center' >"+data[object]['description']+"</td>"+
                "<td class='text-center' >"+data[object]['plastic']+"%</td>"+
                "<td class='text-center' >"+data[object]['glass']+"%</td>"+
                "<td class='text-center' >"+data[object]['cardboard']+"%</td>"+
                "<td class='text-center' >"+data[object]['metal']+"%</td>"+
                "<td class='text-center' >"+data[object]['trash']+"%</td>"+
                "<td class='text-center' >"+data[object]['paper']+"%</td>"+
              "</tr>"
            ;
          }

          $('#conenido_modal').html(contenido);
        }
      }
  });
  $('#exampleModal').modal('show');
}



$('#busqueda_recolectores').submit(function(e){
    e.preventDefault();
    var form = $(this);
    var actionUrl = form.attr('action');
    $.ajax({
        type: "GET",
        url: actionUrl,
        data: form.serialize(), // serializes the form's elements.
        success: function(data)
        {

          document.getElementById('recolectores').innerHTML = '';
          
          var nuevos_recolectores = "";
          
          
          for (const property in data) {
            nombre = '';
            if(data[property]['company_name'] == ''){
              nombre = data[property]['username'];
            }else{
              nombre = data[property]['company_name'];
            }
            descripcion = 'No tiene descripción';
            if(data[property]['description'] != ''){
              descripcion = data[property]['description'];
            }
            texto_residuos = '';
            if(data[property]['plastic'] == true){
              texto_residuos+= '<li class="text-left">Plastico</li>';
            }
            if(data[property]['glass'] == true){
              texto_residuos+= '<li class="text-left">Vidrio</li>';
            }
            if(data[property]['cardboard'] == true){
              texto_residuos+= '<li class="text-left">Cartón</li>';
            }
            if(data[property]['metal'] == true){
              texto_residuos+= '<li class="text-left">Metal</li>';
            }
            if(data[property]['trash'] == true){
              texto_residuos+= '<li class="text-left">Organicos</li>';
            }
            if(data[property]['paper'] == true){
              texto_residuos+= '<li class="text-left">Papel</li>';
            }

            nuevos_recolectores += 
            '<div class="col-12 col-sm-12 col-md-4 mb-2">'+
              '<div class="card text-center border" style="height:100%;">'+
                  '<div class="card-header text-center text-uppercase justify-content-center">'+
                      nombre+
                  '</div>'+
                  '<div class="card-body">'+
                      
                      '<p class="card-text">'+
                        descripcion+
                      '</p>'+
                      '<h4 class="card-text">Residuos que recolectan</h4>'+
                      '<ul class="lista_residuos">'+
                        texto_residuos+
                      '</ul>'+
                  '</div>'+
                  '<div class="card-footer">'+
                      '<button type="button" class="btn btn-primary m-1">Aceptar</button>'+
                      '<button type="button" class="btn btn-secondary m-1">Rechazar</button>'+
                  '</div>'+
              '</div>'+
            '</div>'
          };
          
          document.getElementById('recolectores').innerHTML = nuevos_recolectores;

        }
    });
});