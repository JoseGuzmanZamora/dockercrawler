module.exports = {
    hellom: function() {
        const myModule = require('./test3');
        let val = myModule.helloss(); // val is "Helloss"   

        const mymodules = require('./test4');
        let valu = mymodules.hellosss(); // val is "Hellosss"

        const mymodulesus = require('./test6');
        let valu = mymodulesus.hellow(); // val is "Hellow"
    }
}