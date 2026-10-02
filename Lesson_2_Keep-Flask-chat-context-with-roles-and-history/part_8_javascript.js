$("#chat-form").on("submit", function (e) {

  e.preventDefault();

  var rawText = $("#text").val();

  $.get("/get", { msg: rawText }).done(function (data) {

    $("#chatbox").append(

      "<p><b>You:</b> " + rawText + "</p>"

    );

    $("#chatbox").append(

      "<p><b>FixFlow:</b> " + data + "</p>"

    );

    $("#text").val("");

  });

});
