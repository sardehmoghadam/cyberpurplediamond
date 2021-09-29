function openForm() {
	  document.getElementById("myForm").style.display = "block";
	}

	function closeForm() {
	  document.getElementById("myForm").style.display = "none";
	}

function openregisterForm() {
	  document.getElementById("registerForm").style.display = "block";
	}

	function closeregisterForm() {
	  document.getElementById("registerForm").style.display = "none";
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

var openPage = function(pageName, elmnt, color) {
  // Hide all elements with class="tabcontent" by default */
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Remove the background color of all tablinks/buttons
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }

  // Show the specific tab content
  document.getElementById(pageName).style.display = "block";

  // Add the specific color to the button used to open the tab content
  elmnt.style.backgroundColor = color;


}

var openMenu = function(pageName, elmnt, color) {
  // Hide all elements with class="tabcontent" by default */
  var i, firsttabcontent, firsttablinks;
  tabcontent = document.getElementsByClassName("firsttabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Remove the background color of all tablinks/buttons
  tablinks = document.getElementsByClassName("firsttablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }

  // Show the specific tab content
  document.getElementById(pageName).style.display = "block";

  // Add the specific color to the button used to open the tab content
  elmnt.style.backgroundColor = color;
  document.getElementById(pageName).innerHTML='<object type="type/html" data="temp/mitrehtml.html" ></object>';


}

var openMenu1 = function(pageName, elmnt, color) {
  // Hide all elements with class="tabcontent" by default */
  var i, firsttabcontent, firsttablinks;
  tabcontent = document.getElementsByClassName("firsttabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Remove the background color of all tablinks/buttons
  tablinks = document.getElementsByClassName("firsttablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }

  // Show the specific tab content
  document.getElementById(pageName).style.display = "block";

  // Add the specific color to the button used to open the tab content
  elmnt.style.backgroundColor = color;
    pageName.InnerHtml = "/templates/temp/mitrehtml.html";

}




  document.getElementById("defaultOpen").click();

    (function($) {
      $('#lazyLoadLink').on('click', function() {
        var link = $(this);
        var page = link.data('page');
        $.ajax({
          type: 'post',
          url: '/lazy_load_posts/',
          data: {
            'page': page,
            'csrfmiddlewaretoken': window.CSRF_TOKEN // from index.html
          },
          success: function(data) {
            // if there are still more pages to load,
            // add 1 to the "Load More Posts" link's page data attribute
            // else hide the link
            if (data.has_next) {
                link.data('page', page+1);
            } else {
              link.hide();
            }
            // append html to the posts div
            $('#div').append(data.posts_html);
          },
          error: function(xhr, status, error) {
            // shit happens friends!
          }
        });
      });
    }(jQuery));

var waitingclient = function() {

    document.getElementById('waitingclient').style.display = "block";
}