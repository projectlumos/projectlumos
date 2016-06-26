$(document).ready(function() {

    function getId(url) {
        var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
        var match = url.match(regExp);

        if (match && match[2].length == 11) {
            return match[2];
        } else {
            return 'error';
        }
    }

   //function is used to change the desc based on what ever is clicked
    $(".changeDesc").click(function(){

        var desc = $(this).data("desc");
        var relatedDomains = $(this).data("related-domain");
        var relatedTechnologies = $(this).data("related-technologies");
        var centralActivity = $(this).data("centralActivity");
        var yt_link = $(this).data("yt-link");
        var term = $(this).text()
        
        if (yt_link){
            //change youtube url 
            //display youtube widget
            console.log("changing the youtube link");
            var yt_converted_link = getId(yt_link);
            console.log(yt_converted_link)
            var youtube_embed_code = '<iframe width="560" height="315" src="//www.youtube.com/embed/' + yt_converted_link + '" frameborder="0" allowfullscreen></iframe>';

            $("#yt-embedded-player").html(youtube_embed_code);
        }

        $("#descHeader").text(term);
        $("#descBox").text(desc);
        
        console.log("type of related domains", typeof(relatedDomains));
        console.log("desc", desc);
        console.log("related domains ", relatedDomains);
        console.log("related technologies", relatedTechnologies);
    }); //changing the desc


    //function launches the wiki modal, changes the it's content
    var change_modal_content = function (input_term){
        
        console.log("changing modal data");
        console.log(input_term);
        var data = {'search-term': input_term};
        var error_msg = "Oh shucks! We could not show this search. Please try manually"
        var wiki_summ = false;
        var related_terms = false;
        
        //refine the related term class hiding process
        //please change all the relevant class names and id names to something more readable.
        $(".modalRelatedTerms").hide();
        $("#modalOtherLinks").hide();
        $("#modalTerm").text(input_term);
        $("#modalDesc").text("unhide the wait gyplh div");
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
                    console.log('---------');
                    console.log(typeof(data['summary_data']['summary_present']));
                    console.log((data['summary_data']['summary_present']));
                    if (data['summary_data']['summary_present'] === true){
                        wiki_summ = data['summary_data']['summary_content'];
                        $("#modalDesc").text(wiki_summ);
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
                    var related_terms_struct = "<div>";  

                    $.each(related_terms, function(term, link) {
                         console.log(term, link);
                         related_terms_struct += "<a href='"+link+"' target='_blank'>"+term+"</a>, ";
                    });
                    related_terms_struct += "</div>";                  


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