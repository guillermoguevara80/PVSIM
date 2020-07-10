/*..............................................................................................
... PARA VALIDAR LOS DATOS .....................................................
.............................................................................................*/
var csrftoken = $.cookie('csrftoken');
function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/*..............................................................................................
... TODOS LOS CURSOS .............................................................
............................................................................................. */
$( "#boton_prod" ).click(function(){
	valor = $( "#id_querycom" ).val();
	respuestproducto(valor)
});

function respuestproducto(valor){
    $.ajax({
        beforeSend : function(xhr, settings){
			if(!csrfSafeMethod(settings.type) && !this.crossDomain){
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		url : "/papers/buscar_paper2/",
		type : "GET",
		data : { valor : valor,},
		success : function(json){

            valor_retornado = "<h2>"+json[0].titulo+"</h2>"
			+ json[0].contenido 



            $('#contenedor_filtrado').html(valor_retornado);
            console.log(json[0].titulo);

		},
		error : function(xhr, errmsg, err){
			console.log('Error en carga de respuesta');
		},
    });
}
