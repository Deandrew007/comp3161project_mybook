<?php
    include_once '/phpIncludes/connect.php';
?>

<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
        <style>
            body {
                font-family: 'Open Sans', sans-serif;
                background: white;
            }
            .profile-container {
                width: 700px;
                height: 100px;
                margin: 0 auto;
                margin-top: 50px;
            }
            .profile-container .profile-menu {
                float: left;
                width: 37%;
                height: 463.5px;
                background: #fff;
                box-shadow: 0 0 25px rgba(0, 0, 0, 0.6);
            }
            .profile-container .profile-menu .image-container {
                width: 70px;
                height: 70px;
                margin: 30px 0 60px 35px;
            }
            .profile-container .profile-menu .image-container img {
                max-width: 200%;
                height: 150%;
                border-radius: 50%;
            }
            .profile-container .profile-menu .image-container img:hover {
                opacity: 0.8;
            }
            .profile-container .profile-menu ul {
                list-style: none;
                margin: 0;
                padding: 0;
            }
            .profile-container .profile-menu ul li {
                padding: 10px 20px;
                font-size: 13px;
            }
            .profile-container .profile-menu ul li:hover, .profile-container .profile-menu ul li.active {
                background: #f7f7f7;
                border-left: solid 5px #e48418;
            }
            .profile-container .profile-menu ul li:last-child {
                margin-top: 50px;
            }
            .profile-container .profile-content {
                width: 63%;
                float: right;
                background: #fff;
                box-shadow: 0 0px 25px rgba(0, 0, 0, 0.2);
            }
            .profile-container .profile-content .actions {
                width: 100%;
                background: linear-gradient(to right, #ff105f, #ffad06);
                height: 40px;
                line-height: 40px;
                color: #fff;
                padding: 20px 0 0px 0;
            }
            .profile-container .profile-content .actions i {
                padding-left: 20px;
                float: left;
                font-size: 20px;
            }
            .profile-container .profile-content .actions i:hover {
                opacity: 0.8;
            }
            .profile-container .profile-content .actions i + i {
                padding-right: 20px;
                float: right;
            }
            .profile-container .profile-content .pic {
                background: linear-gradient(to right, #ff105f, #ffad06);
                text-align: center;
                color: #fff;
                padding: 0px 0px 20px 0px;
            }
            .profile-container .profile-content .pic img {
                width: 90px;
                border-radius: 50%;
            }
            .profile-container .profile-content .pic img:hover {
                opacity: 0.8;
            }
            .profile-container .profile-content .pic h2 {
                font-size: 17px;
                padding: 0;
                margin: 0;
                font-weight: 400;
            }
            .profile-container .profile-content .pic span {
                font-size: 15px;
                font-weight: 300;
            }
            .profile-container .profile-content .summary {
                color: #fff;
            }
            .profile-container .profile-content .summary .content {
                width: 50%;
                float: left;
                text-align: center;
                display: block;
                background: linear-gradient(to right, #e48418 0%, #ffd900 100%);
                padding: 10px 0;
            }
            .profile-container .profile-content .summary .content span {
                display: block;
                font-size: 14px;
                font-weight: 500;
            }
            .profile-container .profile-content .profile-details ul {
                list-style: none;
                padding: 0;
                margin: 0;
                color: #929292;
            }
            .profile-container .profile-content .profile-details ul li {
                line-height: 50px;
                border-bottom: 1px solid #f2f2f2;
                font-weight: 400;
                padding-left: 30px;
                font-size: 14px;
            }
            .profile-container .profile-content .profile-details ul li:hover i {
                color: #056cc6;
            }
            .profile-container .profile-content .profile-details ul li i {
                margin-right: 10px;
            }
            .profile-container .profile-content .profile-details ul li span {
                float: right;
                font-weight: 500;
            }
            .profile-container .profile-content .profile-details ul li span:after {
                content: '\f054';
                font-family: 'FontAwesome';
                font-size: 12px;
                float: right;
                margin-right: 20px; 
                margin-left: 20px;
            }
            
        </style>
    </head>

    <body>
        <div class="profile-container">
            <div class="profile-menu">
                <div class="image-container">
                    <img src="https://www.nailseatowncouncil.gov.uk/wp-content/uploads/blank-profile-picture-973460_1280.jpg" alt="">
                </div>
                <ul>
                    <li class="active">Profile</li>
                    <li>Friends</li>
                    <li>Groups</li>
                    <li>Membership</li>
                    <li>Log out</li>
                </ul>
            </div>
            <div class="profile-content">
                <div class="actions">
                    <i class="fa fa-arrow-left" onclick="location.href='navBar.html'"> 
                    </i>
                </div>
                <div class="pic">
                    <img src="img/fb.png" alt="">
                    <h2>FaceApp</h2>
                    <span>_____________</span>
                </div>
                <div class="summary">
                    <div class="content">
                    <span>233</span>
                    <span>Followers</span>
                    </div>
                    <div class="content">
                    <span>349</span>
                    <span>Following</span>
                    </div>
                </div>
                <div class="profile-details">
                    <ul>
                    <li><i class="fa fa-images"></i>View Posts<span>35</span></li>
                    <li><i class="fa fa-camera"></i>View Photos<span>236</span></li>
                    <!-- <li><i class="fa fa-edit"></i>Texts<span>26</span></li> -->
                    <li><i class="fa fa-comment"></i>Generate Report for Users<span>100</span></li>
                    <li><i class="fa fa-comment"></i>Create Admin Users<span>4</span></li>
                    </ul>
                </div>  
            </div>
        </div>
    </body>
</html>
