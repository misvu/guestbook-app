window.onload = function() {
    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext("2d");

    var ballRadius = 10;

    var x = canvas.width / 2;
    var y = canvas.height - 30;
    var dx = -2;
    var dy = -2;

    var scoreBoardHeight = 35;
    var paddleWidth = 75;
    var paddleHeight = 10;
    var paddleX = (canvas.width - paddleWidth) / 2;

    function drawBall() {
        ctx.beginPath();
        ctx.arc(x, y, ballRadius, 0, Math.PI * 2, false);
        ctx.fillStyle = "white";
        ctx.fill();
        ctx.closePath();
    }

    function drawPaddle() {
        ctx.beginPath();
        ctx.rect(paddleX, canvas.height - (paddleHeight + 40), paddleWidth, paddleHeight);
        ctx.fillStyle = "black";
        ctx.fill();
        ctx.closePath();
    }

    function drawScoreBoardPane() {
        ctx.beginPath();
        ctx.rect(0, 0, canvas.width, scoreBoardHeight);
        ctx.fillStyle = "black";
        ctx.fill();
        ctx.closePath();
    }


    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        drawScoreBoardPane();
        drawPaddle();
        drawBall();
        x += dx;
        y += dy;

        if (x + dx > canvas.width - ballRadius || x + dx < ballRadius) {
            dx = -dx;
        }

        if (y + dy < (ballRadius + scoreBoardHeight)) {
            dy = -dy;
        } else if(y + dy > canvas.height- (ballRadius + scoreBoardHeight + paddleHeight)) {
            if (x > paddleX && x < paddleX + paddleWidth) {
                dy = -dy;
            }
        }


    }

    function mouseMoveHandler(e) {
        var relativeX = e.clientX - canvas.offsetLeft;
        if(relativeX > 0 && relativeX < canvas.width) {
            paddleX = relativeX - paddleWidth/2;
        }
    }

    document.addEventListener("mousemove", mouseMoveHandler, false);
    setInterval(draw, 10);
};



/* ----- SITE NAVIGATION ----- */



function openNav() {
    document.getElementById("mySideNav").style.width = "250px";
}

/* Set the width of the side navigation to 0 */
function closeNav() {
    document.getElementById("mySideNav").style.width = "0";
}

function openLogNav() {
    document.getElementById("loginRegPane").style.width = "250px";
}

/* Set the width of the side navigation to 0 */
function closeLogNav() {
    document.getElementById("loginRegPane").style.width = "0";
}






/*Set the width of the side navigation to 250px */


/*

function openNav() {
    document.getElementsByClassName("mySideNav").style.width = "250px";
}

function closeNav() {
    document.getElementsByClassName("mySideNav").style.width = "0";
}


*/