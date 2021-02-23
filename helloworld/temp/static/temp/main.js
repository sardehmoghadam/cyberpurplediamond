function openForm() {
	  document.getElementById("myForm").style.display = "block";
	}

	function closeForm() {
	  document.getElementById("myForm").style.display = "none";
	}

var check = function() {
  if (document.getElementById('password').value ==
    document.getElementById('confirmpassword').value) {
    document.getElementById('confirmpassword').style.color = 'green';
    document.getElementById('message').innerHTML = 'matching';
  } else {
    document.getElementById('confirmpassword').style.color = 'red';
    document.getElementById('message').innerHTML = 'not matching';
  }
}

var passwordChanged = function() {
        var strength = document.getElementById('password');
        var strongRegex = new RegExp("^(?=.{10,})(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*\\W).*$", "g");
        var mediumRegex = new RegExp("^(?=.{8,})(((?=.*[A-Z])(?=.*[a-z]))|((?=.*[A-Z])(?=.*[0-9]))|((?=.*[a-z])(?=.*[0-9]))).*$", "g");
        var enoughRegex = new RegExp("(?=.{6,}).*", "g");
        var pwd = document.getElementById("password");
        if (pwd.value.length == 0) {
            pwd.innerHTML = 'Type Password';
        } else if (false == enoughRegex.test(pwd.value)) {
            pwd.style.color = 'red';
        } else if (strongRegex.test(pwd.value)) {
            pwd.style.color = 'green';
        } else if (mediumRegex.test(pwd.value)) {
            pwd.style.color = 'orange';
        } else {
            strength.innerHTML = '<span style="color:red">Weak!</span>';
        }
    }
