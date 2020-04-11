con = require("../../config/connection");


module.exports = {
    CreateComment: function (comment, callback) {
        
        con.query(
            "INSERT INTO phone_indicator.comment" +
            " (post_id, comment_body,user_id)" +
            " VALUES ('" + comment.post_id + "','" + comment.comment_body +
            "','" + comment.user_id + "')", callback)
    },
    UpdateComment: function (comment, callback) {
        con.query(
            "update phone_indicator.comment set comment_body = '" +
            comment.comment_body + "' where comment_id = " + comment.comment_id,callback
        )
    },
    DeleteComment: function (comment_id, callback) {
        con.query('DELETE FROM  phone_indicator.comment WHERE comment_id = ?', comment_id, callback)
    },
    ShowComment: function (post_id, callback) {
        con.query('SELECT * FROM phone_indicator.comment WHERE post_id = '+ post_id+" ORDER BY RAND()", callback)
    }
}