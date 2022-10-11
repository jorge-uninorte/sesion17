function validar_formulario(){
    var nombre = document.formularioRegistro.nombre;
    //alert('El nombre es ' + nombre.value);
    var apellidos = document.getElementById("apellidos");
    //alert("el appelido es " + apellidos.value);
    var correo = document.formularioRegistro.correo;

    var formato_email = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (!correo.value.match(formato_email)){
        alert("correo inválido");
    }

    if (correo.value.length < 10){
        alert("Debe ingresar al menos 10 caracteres");
    }
}