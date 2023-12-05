$(document).ready(function(){

    $(".btn-cred").click(function(){
        $(".btn-cred").removeClass("activeclick")

        $(this).addClass("activeclick")
    })


    $(".btn-cred").mouseenter(function(){
        $(".btn-cred").removeClass("activeclick")

        $(this).addClass("activeclick")
    })

})