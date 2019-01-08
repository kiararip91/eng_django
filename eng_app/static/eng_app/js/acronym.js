(function ($) {
    "use strict";

    $('.content-to-show').hide();
    $('.content-to-show-correct').hide();

    var english = $('.acronym');
    var userInput = $('input[name="input-explanation"]');
    var correctExplanation = $('.text-solution');

    $('.skip-btn').on('click',function(){
        location.reload();
    });

    $('.show-solution-btn').on('click',function(){
        $('.content-to-hide').hide();
        $('.content-to-show').show();
    });


    $('.container100-div-btn').on('click',function(){

        var userInputVal = userInput.val();
        var correctExplanationVal = correctExplanation.text();

        console.log("validating... " + userInputVal);
        console.log("against... " + correctExplanationVal);

         if(userInputVal.trim().toLowerCase() == correctExplanationVal.trim().toLowerCase()){
                console.log("ESATTA");
                handleCorrectAnswer();
        }else{
            console.log("SBAGLIATA");
            handleWrongAnswer();
        }

    });


    $(".user-input").on('input',function(e){
        $(".user-input").css('color', 'black');
    });


})(jQuery);


function handleWrongAnswer(){
    $(".user-input").css('color', 'red');

}

function handleCorrectAnswer(){
    $(".user-input").css('color', 'green');
    $(".content-to-hide-correct").hide();
    $(".content-to-show-correct").show();
}
