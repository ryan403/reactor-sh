$(document).ready(function(){
    //do something
    $("#thisButton").click(function(){
        processImage();
    });
});

function processImage() {
    // **********************************************
    // *** Update or verify the following values. ***
    // **********************************************
    $("#RecognitionCardNumber").text("XXXX XXXX XXXX XXXX");
   
    let endpoint = "https://westcentralus.api.cognitive.microsoft.com/";
    if (!subscriptionKey) { throw new Error('Set your environment variables for your subscription key and endpoint.'); }
    
    var uriBase = endpoint + "vision/v2.1/ocr";
    var params = {
        "language": "zh-Hans",
        "detectOrientation": "true"
    };
    // Display the image.
    var sourceImageUrl = document.getElementById("inputImage").value;
    document.querySelector("#sourceImage").src = sourceImageUrl;

    // This operation requires two REST API calls. One to submit the image
    // for processing, the other to retrieve the text found in the image.
    //
    // Make the first REST API call to submit the image for processing.
    $.ajax({
        url: uriBase + "?" + $.param(params),

        // Request headers.
        beforeSend: function(jqXHR){
            jqXHR.setRequestHeader("Content-Type","application/json");
            jqXHR.setRequestHeader("Ocp-Apim-Subscription-Key", subscriptionKey);
        },

        type: "POST",

        // Request body.
        data: '{"url": ' + '"' + sourceImageUrl + '"}',
    })

    .done(function(data) {
        //顯示JSON內容
        $("#responseTextArea").val(JSON.stringify(data, null, 2));
        $("#picDescription").text("");
    })

    .fail(function() {
        //丟出錯誤訊息
        var errorString = (errorThrown === "") ? "Error. " : errorThrown + " (" + jqXHR.status + "): ";
        errorString += (jqXHR.responseText === "") ? "" : jQuery.parseJSON(jqXHR.responseText).message;
        alert(errorString);
    });
};