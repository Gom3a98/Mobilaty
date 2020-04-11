con = require("../../config/connection");

const bcrypt = require('bcryptjs');

module.exports = {
    getAllUsers: function(callback) {
        con.query("SELECT * FROM user", callback)
    },
    getUserById: function( id, callback) {
        con.query('SELECT * FROM phone_indicator.user WHERE id = ?',[id], callback)
    },
    createuser: function(User , callback) {
        con.query(
            "INSERT INTO phone_indicator.user" +
            " (name, email,password,age,address,type)" +
            " VALUES ('"+User.name+"','"+User.email+"','"+hashfun(User.password)
            +"','"+User.age+"','"+User.address+"','"+User.type+"')" , callback )
    },
    removeuser: function(id, callback) {
        con.query('DELETE FROM  phone_indicator.user WHERE id = ?',[id], callback)
    },

    finduserByUserName : function(name  , callback){
        con.query('SELECT * FROM  phone_indicator.user WHERE name = ?',
            [name], callback)
    },
    hashfun : (password)=>{
        return bcrypt.hashSync(password,10);
    },
    compare :(userPassword,hashPassword)=>{
        return bcrypt.compareSync(userPassword, hashPassword);
    },


};
