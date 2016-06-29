$(document).ready(function() {

    $(".firstTransitionElement").click(function(){
      $("#firstTransition").hide();
      $("#secondTransition").show();
      $("#noYoutube").hide();
      $("#youtubeTransition").hide();
      $("#qualityWell").hide();
    });

    

    $(".secondTransitionElement").click(function(){
      
      $("#secondTransition").hide();      
      //checkout for youtube module display
      var is_youtube = $(this).data("yt-link");

      if (is_youtube){
        $("#youtubeTransition").show();
        $("#noYoutube").hide();
      }
      else{
        $("#youtubeTransition").hide();
        $("#noYoutube").show();
      }

      
      //show the quality well
      $("#qualityWell").show();

    });

   
    //quality rating div toggle
    $("#qualityRatingsTrigger").click(function() {
      $("#qualityRatings").slideToggle("slow");
      $(window).scrollTop($('#qualityRatingsTrigger').offset().top-20)

    });


   //function is used to change the desc based on what ever is clicked
    $(".changeDesc").click(function(){

        var resourceName = $(this).data("resource-name");
        var desc = $(this).data("desc");
        var relatedDomains = $(this).data("related-domains");
        var relatedTechnologies = $(this).data("related-techs");
        var centralActivity = $(this).data("centralActivity");
        var yt_link = $(this).data("yt-link");
        var term = $(this).text()

        if (yt_link){
            
            //change youtube url 
            //display youtube widget
            console.log("changing the youtube link");

            var yt_converted_link = yt_link.replace(/(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.+)/g, '<iframe width="560" height="345" src="//www.youtube.com/embed/$1" frameborder="0" allowfullscreen></iframe>');

            //hack
            var youtube_embed_code = yt_converted_link.replace('https://', '');

            console.log(youtube_embed_code);

            $("#yt-embedded-player").html(youtube_embed_code);
            $("#videoTitle").text(resourceName);
        }

        $("#descHeader").text(term);
        $("#descBox").text(desc);
        
        // console.log("type of related domains", typeof(relatedDomains));
        // console.log("related domains ", relatedDomains);

        // console.log("related technologies", relatedTechnologies);
        // 
        // 


        //change quality ratings
        
        var quality_helpfulness = $(this).data("quality-helpfulness");
        var quality_simplicity = $(this).data("quality-simplicity");
        var quality_recommendation = $(this).data("quality-recommendation");
        var quality_placement = $(this).data("quality-placement");

        $("#qualityRatings").hide();


        $("#qualityHelpfulness").attr("aria-valuenow", quality_helpfulness);
        $("#qualityHelpfulness").attr("style", "width: "+quality_helpfulness+"%");

        $("#qualitySimplicity").attr("aria-valuenow", quality_simplicity);
        $("#qualitySimplicity").attr("style", "width: "+quality_simplicity+"%");

        $("#qualityRecommendation").attr("aria-valuenow", quality_recommendation);
        $("#qualityRecommendation").attr("style", "width: "+quality_recommendation+"%");

        $("#qualityPlacement").attr("aria-valuenow", quality_placement);
        $("#qualityPlacement").attr("style", "width: "+quality_placement+"%");

    }); //changing the desc


    //function launches the wiki modal, changes the it's content
    var change_modal_content = function (input_term){
        
        $("#loadingDiv").show();

        console.log("changing modal data");
        console.log(input_term);
        var data = {'search-term': input_term};
        var error_msg = "Oh shucks! We could not show this search. Please try manually"
        var wiki_summ = false;
        var related_terms = false;
        
        //refine the related term class hiding process
        //please change all the relevant class names and id names to something more readable.
        $("#modalDesc").hide();
        $(".modalRelatedTerms").hide();
        $("#modalOtherLinks").hide();
        $("#modalTerm").text(input_term);
        $("#wikki").modal("show");

        $.ajax({
            type : 'POST',
            url : '/search-wiki/',
            data :JSON.stringify(data),
            success : function(data){
                console.log("return data");
                console.log(data);

                //convert json data into an object(dictionary)
                data = $.parseJSON(data);
                
                if (data){
                    // console.log('---------');
                    console.log(typeof(data['summary_data']['summary_present']));
                    console.log((data['summary_data']['summary_present']));
                    if (data['summary_data']['summary_present'] === true){
                        wiki_summ = data['summary_data']['summary_content'];
                        $("#modalDesc").text(wiki_summ);
                        $("#modalDesc").show();
                    }
                    else{
                        var other_links =  data['summary_data']['other_links'];
                        var other_links_struct = "<div>";
                        $.each(other_links, function(term, link) {
                             console.log(term, link);
                             other_links_struct += "<p><a href='"+link+"' target='_blank'>"+term+"</a></p>";
                        });
                        other_links_struct += "</div>";

                        $("#modalOtherLinks").html(other_links_struct);
                        $("#modalOtherLinks").show();
                    }//if other links

                    related_terms = data['related_terms'];                    
                    var related_terms_struct = "<div> | ";  

                    $.each(related_terms, function(term, link) {
                         console.log(term, link);
                         related_terms_struct += "<a class='even_spacing' href='"+link+"' target='_blank'>"+term+"</a> | ";
                    });
                    related_terms_struct += "</div>";

                    $("#loadingDiv").hide();


                    // console.log(related_terms);
                    // console.log(wiki_summ);
                    
                    
                    $("#modalTerms").html(related_terms_struct);
                    $(".modalRelatedTerms").show();

                }//if
                else{
                    $("#modalDesc").text(error_msg);
                }//else
            },
            error : function(data){
                $("#modalDesc").text(error_msg);
            }
        });//ajax call

    };//change_model_content function


    //wiki modal search button
    $("#search-btn").click(function(){
        var search_term = $("#search-term").val().trim()
        console.log(search_term);
        if (search_term){
            console.log('searching wiki');
            $("wikki").modal("hide");
            change_modal_content(search_term);
        }
    });//wiki search button


});//document ready


// SE js
// 
// /* for accordion */
$(document).ready(function() {
  $('.collapse.in').prev('.panel-heading').addClass('active');
  $('#accordion, #bs-collapse')
  .on('show.bs.collapse', function(a) {
    $(a.target).prev('.panel-heading').addClass('active');
  })
  .on('hide.bs.collapse', function(a) {
    $(a.target).prev('.panel-heading').removeClass('active');
  });
    $("#onToggle").click(function(){  //to show or hide progress 
      $("#toggle").slideToggle("slow");
    });
    $(".navbar-toggle").click(function(){  
      $("#left").slideDown("slow");
    });
    $(".btn").click(function(){
      $(".btn-primary").css("box-shadow","none");
    });
  });

//ripple effect for buttons

(function (window, $) {
  $(function() {
    $('.ripple').on('click', function (event) {
      event.preventDefault();
      var $div = $('<div/>'),
      btnOffset = $(this).offset(),
      xPos = event.pageX - btnOffset.left,
      yPos = event.pageY - btnOffset.top;
      $div.addClass('ripple-effect');
      var $ripple = $(".ripple-effect");
      $div
      .css({
        top: yPos - ($ripple.height()/2),
        left: xPos - ($ripple.width()/2),
        background: $(this).data("ripple-color")
      }) 
      .appendTo($(this));

      window.setTimeout(function(){
        $div.remove();
      }, 2000);
    });
  });
})(window, jQuery);

    //to display value of sliders

    function updateTextInput1(val) {
      document.getElementById('textInput1').innerHTML=val; 
    }
    function updateTextInput2(val) {
      document.getElementById('textInput2').innerHTML=val; 
    }
    function updateTextInput3(val) {
      document.getElementById('textInput3').innerHTML=val; 
    }
    function updateTextInput4(val) {
      document.getElementById('textInput4').innerHTML=val; 
    }