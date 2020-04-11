var express = require('express');
var router = express.Router();

var user = require("../app/controllers/user/UserController")

var notify = require('../app/controllers/GeneralControllers/notfiy');
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});
router.get('/login', user.loginGet);
router.post('/login', user.loginPost);

router.get('/signup',user.signupGet);
router.post('/signup',user.signupPost);

router.get('/profile',user.showProfile);
router.get('/checkUserName',user.checkUserName);


router.post('/updateComment',user.UpdateComment);
router.post('/createComment',user.CreateComment);
router.get('/deleteComment',user.DeleteComment);
router.get('/getComments',user.ShowComment);



router.get('/notifcation',notify.selectAllNotify)
router.get('/notifcationDetails',notify.selectSpecificNotify)



module.exports = router;
