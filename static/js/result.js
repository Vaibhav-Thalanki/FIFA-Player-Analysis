document.addEventListener("DOMContentLoaded", (event) => {
    if (
      document.querySelector("h1").textContent ==
      "The prediction is that the player is of Attack Position"
    ) {
      document.querySelector("img").src = "./static/images/attack.jpg";
      document.querySelector("p").innerHTML = 'ST (Striker) <br>RW (Right Wing) <br> LW (Left Wing)<br> RM (Right Mid)<br> CM (Center Mid)<br> LM (Left Mid)<br> CAM (Center Attacking Mid)<br> CF (Center Forward) ';
    } else {
      document.querySelector("img").src = "./static/images/defence.jpg";
      document.querySelector("p").innerHTML = 'CDM (Center Defensive Mid) <br> CB (Center Back)<br> LB (Left Back)<br> RB (Right Back)<br> RWB (Right Wing Back)<br> LWB (Left Wing Back) ';
    }
  });