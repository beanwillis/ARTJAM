<?php
    session_start();
    $interest = $_SESSION['interest'];
    if (!isset( $_GET['skill'])) {
        header('Location: wheel2.php');
    } else {
        $skill = $_GET['skill'];
        $_SESSION['skill'] = $skill;
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
            <div class="progress-bar bg-info" role="progressbar" style="width: 25%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <p class="lead text-center mt-3">Please select an <strong>issue</strong> that is most relevant to you.</p>
        <form action="wheel3.php" method="get">
            <div class="btn-group-vertical mt-10" style="width:100%">
                <button id="education" onClick="selection(this.id)" type="button" class="btn btn-secondary mb-3" style="background-color: #4a8bae;white-space: normal;">
                    <h4 class="display-5">Education & Mobility</h4>
                    <p class="font-weight-normal">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </button>
                <button id="equality" onClick="selection(this.id)" type="button" class="btn btn-secondary mb-3" style="background-color: #4a8bae;white-space: normal;">
                    <h4 class="display-5">Equality & Diversity</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </button>
                <button id="environment" onClick="selection(this.id)" type="button" class="btn btn-secondary mb-3" style="background-color: #4a8bae;white-space: normal;">
                    <h4 class="display-5">Environment & Sustainability</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </button>
                <button id="health" onClick="selection(this.id)" type="button" class="btn btn-secondary mb-3" style="background-color: #4a8bae;white-space: normal;">
                    <h4 class="display-5">Health & Wellbeing</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </button>
                <button id="cybersecurity" onClick="selection(this.id)" type="button" class="btn btn-secondary mb-3" style="background-color: #4a8bae;white-space: normal;">
                    <h4 class="display-5">Cybersecurity</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </button>
            </div>
        </form>
        <button type="button" class="btn btn-default btn-sm" style="font-size: 50px;background-color: #fdf6ee;border: none; width:70px; height:70px; border-radius:50%;">
            <a href="wheel2.php?interest=<?php echo $interest; ?>" style="color:inherit"><span class="glyphicon glyphicon-circle-arrow-left"></span></a>
        </button>
    </div>

    <script>
        function selection(clicked) {
            // var url = "wheel3.php?issue=" + clicked;
            // document.location.href = url;
            sessionStorage.setItem("issue", clicked);
        }
    </script>
</body>
</html>