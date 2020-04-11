con = require("../../config/connection");


module.exports = {
    CreatePost : (Post , callback )=>{
        con.query("INSERT INTO phone_indicator.post" +
        " (post_description , post_img ,store_id) VALUES (?,?,?)" , 
        [Post.post_description , Post.post_img , Post.store_id],callback)
    },
    DeletePost : (id ,callback)=>{
        con.query("DELETE FROM phone_indicator.post WHERE post_id =?" , [id] , callback)
    },
    UpdatePost : (Post ,callback)=>{
        con.query("UPDATE phone_indicator.post " +
        " SET post_description = ?, post_img = ? WHERE  store_id = ?" , 
        [Post.post_description , Post.post_img , Post.store_id],callback)
    },
    findById : (id ,callback)=>{
        con.query("SELECT * FROM phone_indicator.post WHERE post_id =?" , [id] , callback)
    },
    findByStoreId : (store_id ,callback)=>{
        con.query("SELECT * FROM phone_indicator.post WHERE store_id =?" , [store_id] , callback)
    },
    findAll : (callback)=>{
        con.query("SELECT * FROM phone_indicator.post" , callback)
    }
    
}