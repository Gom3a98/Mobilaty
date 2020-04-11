var mysql = require('mysql');
var con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '12345678',
  database: 'phone_indicator'
});
con.connect((err)=> {
  if (err) throw err;
  console.log("Connected!");
});


module.exports= con ;

