/**
 * Created by Edwar Amaya on 22/10/2016.
 */
$(".rotar").click(function(){
    $(".ion-ios-reload").addClass("down");
    setTimeout(function () {
        $(".down").toggleClass("down");
    }, 5000);
});