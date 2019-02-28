<?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "mydb";
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$link = $_REQUEST['link'];
$prerequest = $_REQUEST['prerequest'];
$latency = $_REQUEST['latency'];
$server = $_REQUEST['server'];
$domloading = $_REQUEST['domloading'];
$domcomplete = $_REQUEST['domcomplete'];
$loadtime = $_REQUEST['loadtime'];
$total = $_REQUEST['total'];

$sql = "INSERT INTO data(link,prerequest,latency,server,domloading,domcomplete,loadtime,total) VALUES ('$link','$prerequest','$latency','$server','$domloading','$domcomplete','$loadtime','$total')";
if ($conn->query($sql) === TRUE) {
    echo "Inserted";
} else {
    echo "Error creating database: " . $conn->error;
}
//http://localhost/connect.php?link=ohio&prerequest=987&latency=90&server=121&domloading=567&domcomplete=123&loadtime=112&total=111
//http://localhost/connect.php?answers=ohoogoogogoasdasda
$conn->close();
?> 
