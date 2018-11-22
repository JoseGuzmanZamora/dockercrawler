module.exports = {
    hellow: function () {
        class User {

            constructor(name) {
                this.name = name;
            }

            sayHi() {
                alert(this.name);
            }



        }

        function cargaImagen(input) {
            var target = input.target;
            if (target.files && target.files[0]) {
                var reader = new FileReader();
                reader.readAsDataURL(target.files[0]);
                if (target.files && target.files[0]) {
                    reader.onload = function (e) {
                        setTimeout(function () {
                            $("#imgCategoria").attr('src', e.target.result);
                        }, 300);

                    };
                }
            }
        }

        function agregarPregunta() {
            bloquear();

            var nombre = $("#txtPregunta").val();
            var categoria = $("#cbxCategoria").val();
            var dificultad = $("#divDificultad").find(".btn-outline-secondary.active").find("input:radio:first").val();

            var data = new Object();
            data.pregunta = nombre;
            data.estado = "ALTA";
            data.categoria = categoria;
            data.dificultad = dificultad;
            data.pregunta = $("#txtPregunta").val();



            var respuesta = new Object();
            respuesta.respuestas = [];
            var index = 0;
            var resp = null;

            var tipo = $("#cbxTipoPregunta").val();
            /*Tipo verdadero y falso*/
            if (tipo == 1) {
                data.tipopregunta = 1;
                var correcta = 0;
                if ($("#rdoVerdadero").prop('checked') == true) {
                    correcta = 1;
                }
                resp = new Object();
                resp.respuesta = "";
                resp.correcta = correcta;
                respuesta.respuestas[0] = resp;

            } else if (tipo == 2) { // tipo opcion múltiple, única opción
                data.tipopregunta = 2;
                //respuesta 1
                resp = new Object();
                resp.respuesta = $("#txtRespM1").val();
                resp.correcta = $("#chkResp1").prop('checked') == true ? 1 : 0;
                respuesta.respuestas[0] = resp;

                //respuesta 2
                resp = new Object();
                resp.respuesta = $("#txtRespM2").val();
                resp.correcta = $("#chkResp2").prop('checked') == true ? 1 : 0;
                respuesta.respuestas[1] = resp;

                //respuesta 3
                resp = new Object();
                resp.respuesta = $("#txtRespM3").val();
                resp.correcta = $("#chkResp3").prop('checked') == true ? 1 : 0;
                respuesta.respuestas[2] = resp;

                //respuesta 4
                resp = new Object();
                resp.respuesta = $("#txtRespM4").val();
                resp.correcta = $("#chkResp4").prop('checked') == true ? 1 : 0;
                respuesta.respuestas[3] = resp;

            } else if (tipo == 3) {
                data.tipopregunta = 3;
                //respuesta 1
                resp = new Object();
                resp.respuesta = $("#txtRespU1").val();
                resp.correcta = $("#rdoResp1").prop('checked') == true ? 1 : 0;
                respuesta.respuestas[0] = resp;

                //respuesta 2
                resp = new Object();
                resp.respuesta = $("#txtRespU2").val();
                resp.correcta = $("rdoResp2").prop('checked') == true ? 1 : 0;
                respuesta.respuestas[1] = resp;

                //respuesta 3
                resp = new Object();
                resp.respuesta = $("#txtRespU3").val();
                resp.correcta = $("#rdoResp3").prop('checked') == true ? 1 : 0;
                respuesta.respuestas[2] = resp;

                //respuesta 4
                resp = new Object();
                resp.respuesta = $("#txtRespU4").val();
                resp.correcta = $("#rdoResp4").prop('checked') == true ? 1 : 0;
                respuesta.respuestas[3] = resp;

            }

            let user = new User("Fernando");
            user.sayHi();
        }
    }
}