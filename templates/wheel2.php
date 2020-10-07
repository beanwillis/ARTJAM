<?php
    session_start();
    if (!isset( $_GET['interest'])) {
        header('Location: wheel1.html');
    } else {
        $interest = $_GET['interest'];
        $_SESSION['interest'] = $interest;
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet'>
    <link rel="stylesheet" href="progress-tracker.css">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body style="background-color: #fdf6ee;">
    <style>
        .btn-secondary:focus {
            background-color: #ea755a !important;
            color: white;
            box-shadow: none!important;
            border: none;
        }
    </style>
    
    <div class="container mt-4">
        <span class="glyphicon glyphicon-home" style="font-size:20px;"></span>
        <div class="progress">
            <div class="progress-bar" role="progressbar" style="width: 25%" aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"></div>
            <div class="progress-bar bg-success" role="progressbar" style="width: 25%" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <p class="lead text-center mt-3">Please select a <strong>skill</strong> that is most relevant to you.</p>
        <form action="wheel3.php" method="get">
            <div class="btn-group-vertical mt-10" style="width:100%">
                <button id="social" onClick="selection(this.id)" type="button" class="btn btn-secondary mb-3" style="background-color: #4a8bae;white-space: normal;">
                    <h4 class="display-5">Social</h4>
                    <p class="font-weight-normal">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </button>
                <button id="creative" onClick="selection(this.id)" type="button" class="btn btn-secondary mb-3" style="background-color: #4a8bae;white-space: normal;">
                    <h4 class="display-5">Creative</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </button>
                <button id="business" onClick="selection(this.id)" type="button" class="btn btn-secondary mb-3" style="background-color: #4a8bae;white-space: normal;">
                    <h4 class="display-5">Business</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </button>
                <button id="leadership" onClick="selection(this.id)" type="button" class="btn btn-secondary mb-3" style="background-color: #4a8bae;white-space: normal;">
                    <h4 class="display-5">Leadership</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </button>
                <button id="technology" onClick="selection(this.id)" type="button" class="btn btn-secondary mb-3" style="background-color: #4a8bae;white-space: normal;">
                    <h4 class="display-5">Technology</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </button>
            </div>
        </form>
        <button type="button" class="btn btn-default btn-sm" style="font-size: 50px;background-color: #fdf6ee;border: none; width:70px; height:70px; border-radius:50%;">
            <a href="wheel1.html" style="color:inherit"><span class="glyphicon glyphicon-circle-arrow-left"></span></a>
        </button>
    </div>

    <script>
        function selection(clicked) {
            // var url = "wheel3.php?skill=" + clicked;
            // document.location.href = url;
            sessionStorage.setItem("skill", clicked);
        }
    </script>
</body>
</html>