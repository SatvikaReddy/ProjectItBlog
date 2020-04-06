<?php
$con= mysqli_connect('localhost' , 'root' , 'qwer123');
mysqli_select_db($con,"student");

$email=$_POST['email'];
$password=$_POST['pwd'];
$s= "select * from user where email='$email' and pwd='$password'";
$result= mysqli_query($con,$s);
$num= mysqli_num_rows($result);

if($num == 1){
    header("location: projects.html");
}
else{
    header("location: login.html");
} 
?>