module.exports = {
    
    hello: function () {
        let user = new User("Fernando");
        user.sayHi();
        
        console.log("Hello");
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
    }
    
}