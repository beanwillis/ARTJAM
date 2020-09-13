<?php
    if (!isset( $_GET['interest'])) {
        header('Location: wheel1.html');
    } else {
        $interest = $_GET['interest'];
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="wheel.css">
    <link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet'>
    <link rel="stylesheet" href="progress-tracker.css">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div class="progress">
        <div class="progress-bar" role="progressbar" style="width: 25%" aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"></div>
        <div class="progress-bar bg-success" role="progressbar" style="width: 25%" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100"></div>
    </div>
    <p class="header text-center">Please select a <strong>skill</strong> that is most relevant to you.</p>
    <form action="wheel3.php" method="get">
        <div class="container">
            <img src="../static/img/social.png" alt="Social">
            <button name="skill" value="social" onclick="window.location.href='wheel3.php';" class="btn" style="background-color: #91e2f0;color: black;">Social</button>
        </div>
        <div class="container">
            <img src="../static/img/creative.jpg" alt="Creative">
            <button name="skill" value="creative" onclick="window.location.href='wheel3.php';" class="btn" style="background-color: #fbd743;color: black;">Creative</button>
        </div>
        <div class="container">
            <img src="../static/img/business.jpeg" alt="Business">
            <button name="skill" value="business" onclick="window.location.href='wheel3.php';" class="btn" style="background-color: #edbc84;color: black;">Business</button>
        </div>
        <div class="container">
            <img src="../static/img/leadership.png" alt="Leadership">
            <button name="skill" value="leadership" onclick="window.location.href='wheel3.php';" class="btn" style="background-color: #99c1dc;color: black;">Leadership</button>
        </div>
        <div class="container">
            <img src="../static/img/technology.jpeg" alt="Technology">
            <button name="skill" value="technology" onclick="window.location.href='wheel3.php';" class="btn" style="background-color: #074763;color: white;">Technology</button>
        </div>
        <input type="hidden" name="interest" value="<?php echo $interest ?>">
    </form>
    <a href="wheel1.html" class="previous">&#8249;</a>
    <!-- <a href="wheel3.php" class="next">&#8250;</a> -->
</body>
</html>