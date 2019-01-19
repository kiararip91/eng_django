(function ($) {
    "use strict";

    $('.content-to-show').hide();
    $('.content-to-show-correct').hide();

    var english = $('.acronym');
    var userInput = $('input[name="input-explanation"]');
    var correctExplanation = $('.text-solution');

    var index = 0;

    $(function(){
        setupUI();
    });


    function setupUI(){
        if(index++ != parsedAcronyms.length ){

            console.log(parsedAcronyms[index]);
            console.log(parsedAcronyms[index].name);

            userInput.val("");
            english.text(parsedAcronyms[index].name);
            correctExplanation.text(parsedAcronyms[index].explanation.split("---").join("'"));

            $('.content-to-hide').show();
            $('.content-to-show').hide();
            $('.content-to-show-correct').hide();

        }else{
             window.location.href = "http://localhost:8000/eng/acronyms";
        }
    }

    $('.skip-btn').on('click',function(){
        setupUI();
    });

    $('.show-solution-btn').on('click',function(){
        $('.content-to-hide').hide();
        $('.content-to-show').show();
    });


    $('.container100-div-btn').on('click',function(){

        var userInputVal = userInput.val();
        var correctExplanationVal = correctExplanation.val();

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

    function handleWrongAnswer(){
        $(".user-input").css('color', 'red');
    }

    function handleCorrectAnswer(){
        $(".user-input").css('color', 'green');
        $(".content-to-hide-correct").hide();
        $(".content-to-show-correct").show();
    }


})(jQuery);
