function myFunction() {
        var x = document.getElementById("passwordd");
        if (x.type === "password") {
          x.type = "text";
        } else {
          x.type = "password";
        }
      }
function myFunction2() {
        var x = document.getElementById("password2");
        if (x.type === "password") {
          x.type = "text";
        } else {
          x.type = "password";
        }
      }
      
function checkPassword(){
        let password = document.getElementById("password").value;
        let email = document.getElementById("username").value;
        let cnfrmPassword = document.getElementById("cnfrm-password").value;
        console.log(" Password:", password,'\n',"Confirm Password:",cnfrmPassword);
        let message = document.getElementById("message");
        let sentence = document.getElementById("username").value;
       
      

        if(password.length != 0){
          
            if(password == cnfrmPassword){
                if(email !=0 ){
                  
                  var check = sentence.toString().includes('.com');
                  

                    if(check == true){

                     
                      document.location = '/global/loading/i-phone1313pro3.html'; 

                    }
                    else{
                      message.textContent = "The e-mail format isn't correct";

                    }

                }
                else {
                  message.textContent = "Email can't be empty";
                }
                
            }
            else{
                message.textContent = "Password don't match";
                
            }
        }

        else{
            if(email !=0 ){
              message.textContent = "Password can't be empty";
            }
            else {
            message.textContent = "Email & Password can't be empty";
        }
    }
  }
