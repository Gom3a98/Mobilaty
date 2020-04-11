var Student = require("../../model/User");

var formidable = require('formidable');
//http://localhost:3000/startExam/admin/9/1
const fs = require('fs-extra');

var Authentication = async (req, res) => {

	if (!req.session.userName && req.session.type==null)
		return false;
	else
		return true;
}

module.exports = {
	signupGet: (req, res, next) => {
		req.session.destroy();
		res.render('user/userSignUp', { title: 'Sign Up' });
	},
	signupPost: (req, res) => {
		Student.createStudent(req.body, function (err) {
			if (err) throw err;
			req.session.userName = req.body.name;
			res.send(req.body)
		});
	},
	loginPost: (req, res, next) => {
		var username = req.body.userName;
		var x = Student.findStudentByUserName(username, (err, result) => {
			if (result.length == 1 && Student.compare(req.body.password, result[0].password)) {
				req.session.userName = username;
				req.session.studentId = result[0].id;
				res.send(result)

			}
			else
			    res.send({'success' : false});
		});
	},
	loginGet: (req, res, next) => {
		req.session.destroy();
		res.render('user/login', { title: 'Login' })
	},
	showProfile: async (req, res, next) => {

		if (await Authentication(req, res)) {
			Position.getAllPositions(function (err, results) {
				res.render("user/profile", {
					username: req.session.userName,
					positions: results

				});
			});
		}
		else
			res.redirect('/login')
		//Authentication(req,res).then(res.send('Welcome back, ' + req.session.userName + '!'));
	},

	checkUserName:function(req,res,next){
		var userName = req.query.userName ;
		console.log(userName[0])
		Student.searchCandUserName(userName[0], (err, result) => {
			if (err) throw err;
			console.log(result)
			if (result.length == 0)
				res.send('1');
			else
				res.send('0');
		})
	},
};