$(document).ready(function(){
    /* SLIDER */
    $('.slider').slider({full_width: true, indicators:false});
    // Initialize collapse button
    $(".button-collapse").sideNav();
    // Initialize collapsible (uncomment the line below if you use the dropdown variation)
    //$('.collapsible').collapsible();
    $('.collapsible').collapsible({
        accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
    });
    /* SCROLLSPY */
    $('.scrollspy').scrollSpy();
    /* VIDEOS */
    $('#my-video').backgroundVideo();
    $('ul.tabs').tabs();
    /* CUENTA REGRESIVA */

    /* PROGRESS */

    //Botones $5
    $("#cupon-5").click(function(){
        $("#cupon-5").fadeOut("slow");
        $("#paypal-5").fadeOut("slow");
        $("#transfer-5").fadeOut("slow");
        $("#input-cupon-5").fadeIn("slow");
        $("#boton-env-5").fadeIn("slow");
        $("#boton-can-5").fadeIn("slow");
    });
    $("#boton-can-5").click(function(){
        $("#cupon-5").fadeIn("slow");
        $("#paypal-5").fadeIn("slow");
        $("#transfer-5").fadeIn("slow");
        $("#input-cupon-5").fadeOut("slow");
        $("#boton-env-5").fadeOut("slow");
        $("#boton-can-5").fadeOut("slow");
    });
    //Botones $20
    $("#cupon-20").click(function(){
        $("#cupon-20").fadeOut("slow");
        $("#paypal-20").fadeOut("slow");
        $("#transfer-20").fadeOut("slow");
        $("#input-cupon-20").fadeIn("slow");
        $("#boton-env-20").fadeIn("slow");
        $("#boton-can-20").fadeIn("slow");
    });
    $("#boton-can-20").click(function(){
        $("#cupon-20").fadeIn("slow");
        $("#paypal-20").fadeIn("slow");
        $("#transfer-20").fadeIn("slow");
        $("#input-cupon-20").fadeOut("slow");
        $("#boton-env-20").fadeOut("slow");
        $("#boton-can-20").fadeOut("slow");
    });
    //Botones $100
    $("#cupon-100").click(function(){
        $("#cupon-100").fadeOut("slow");
        $("#paypal-100").fadeOut("slow");
        $("#transfer-100").fadeOut("slow");
        $("#input-cupon-100").fadeIn("slow");
        $("#boton-env-100").fadeIn("slow");
        $("#boton-can-100").fadeIn("slow");
    });
    $("#boton-can-100").click(function(){
        $("#cupon-100").fadeIn("slow");
        $("#paypal-100").fadeIn("slow");
        $("#transfer-100").fadeIn("slow");
        $("#input-cupon-100").fadeOut("slow");
        $("#boton-env-100").fadeOut("slow");
        $("#boton-can-100").fadeOut("slow");
    });
    //Botones $500
    $("#cupon-500").click(function(){
        $("#cupon-500").fadeOut("slow");
        $("#paypal-500").fadeOut("slow");
        $("#transfer-500").fadeOut("slow");
        $("#input-cupon-500").fadeIn("slow");
        $("#boton-env-500").fadeIn("slow");
        $("#boton-can-500").fadeIn("slow");
    });
    $("#boton-can-500").click(function(){
        $("#cupon-500").fadeIn("slow");
        $("#paypal-500").fadeIn("slow");
        $("#transfer-500").fadeIn("slow");
        $("#input-cupon-500").fadeOut("slow");
        $("#boton-env-500").fadeOut("slow");
        $("#boton-can-500").fadeOut("slow");
    });
    //Botones $1000
    $("#cupon-1000").click(function(){
        $("#cupon-1000").fadeOut("slow");
        $("#paypal-1000").fadeOut("slow");
        $("#transfer-1000").fadeOut("slow");
        $("#input-cupon-1000").fadeIn("slow");
        $("#boton-env-1000").fadeIn("slow");
        $("#boton-can-1000").fadeIn("slow");
    });
    $("#boton-can-1000").click(function(){
        $("#cupon-1000").fadeIn("slow");
        $("#paypal-1000").fadeIn("slow");
        $("#transfer-1000").fadeIn("slow");
        $("#input-cupon-1000").fadeOut("slow");
        $("#boton-env-1000").fadeOut("slow");
        $("#boton-can-1000").fadeOut("slow");
    });
    //Transfer
    $('.modal-trigger').leanModal();

});
$('.parallax').parallax();

