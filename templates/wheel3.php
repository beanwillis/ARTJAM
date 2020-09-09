<?php
    if (!isset( $_GET['skill']) && isset($_GET['interest'])) {
        header('Location: wheel2.html');
    } else {
        $skill = $_GET['skill'];
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
        <div class="progress-bar bg-info" role="progressbar" style="width: 25%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
    </div>
    <p class=" header text-center">Please select an <strong>issue</strong> that is most relevant to you.</p>
    <form action="final.php" method="get">
        <div class="container">
            <img src="../static/img/education.jpg" alt="Education & Mobility">
            <button name="issue" value="education-mobility" onclick="window.location.href='final.php';" class="btn" style="background-color: #faeac6;color: black;">Education & Mobility</button>
        </div>
        <div class="container">
            <img src="../static/img/equality.jpg" alt="Equality & Diversity">
            <button name="issue" value="equality-diversity" onclick="window.location.href='final.php';" class="btn" style="background-color: #ffdfa2;color: black;">Equality & Diversity</button>
        </div>
        <div class="container">
            <img src="../static/img/environment.jpg" alt="Environment & Sustainability">
            <button name="issue" value="environment-sustainability" onclick="window.location.href='final.php';" class="btn" style="background-color: #1f8e26;color: white;">Environment & Sustainability</button>
        </div>
        <div class="container">
            <img src="../static/img/health-wellbeing.jpg" alt="Health & Wellbeing">
            <button name="issue" value="health-wellbeing" class="btn" style="background-color: #d1cabf;color: black;">Health & Wellbeing</button>
        </div>
        <div class="container">
            <img src="../static/img/cybresecurity.jpg" alt="Cybersecurity">
            <button name="issue" value="cybersecurity" class="btn" style="background-color: #0a3853;color: white;">Cybersecurity</button>
        </div>
        <input type="hidden" name="interest" value="<?php echo $interest ?>">
        <input type="hidden" name="skill" value="<?php echo $skill ?>">
    </form>
    <a href="wheel2.php" class="previous">&#8249;</a>
    <!-- <a href="final.php" class="next">&#8250;</a> -->
</body>
</html>