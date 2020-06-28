$(document).ready(function(){
    //do something
    $("#thisButton").click(function(){
        processTranslate();
    });
});

function processTranslate() {
    //修改網址的第一個單字為你的服務網域
    let uriBase = "https://YOUR_DOMAIN_NAME.cognitiveservices.azure.com/translator/text/v3.0/translate";
    let params = {
        "api-version": 3.0,
        "from": "en",
        "to": "zh-Hans",
    };
    //顯示分析的圖片
    let sourceTranslateText = document.getElementById("inputText").value;
    
    //送出分析
    $.ajax({
        url: uriBase + "?" + $.param(params),
        // Request header
        beforeSend: function(xhrObj){
            xhrObj.setRequestHeader("Content-Type","application/json");
            xhrObj.setRequestHeader("Ocp-Apim-Subscription-Key", subscriptionKey);
        },
        type: "POST",
        // Request body
        data: '[{"Text": ' + '"' + sourceTranslateText + '"}]',
    })
    .done(function(data) {
        //顯示JSON內容
        $("#responseTextArea").val(JSON.stringify(data, null, 2));
        //修改下面這一行將翻譯結果顯示於右方
        $("#translateResult").text();
    })
    .fail(function(jqXHR, textStatus, errorThrown) {
        //丟出錯誤訊息
        var errorString = (errorThrown === "") ? "Error. " : errorThrown + " (" + jqXHR.status + "): ";
        errorString += (jqXHR.responseText === "") ? "" : jQuery.parseJSON(jqXHR.responseText).message;
        alert(errorString);
    });
};