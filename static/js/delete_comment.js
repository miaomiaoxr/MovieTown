$(".delete_link").on("click",function(e){
    e.preventDefault();
    const $this = $(this);
    if(confirm("Are you sure to DELETE this comment?")){

        function getCookie(cname) {
            var name = cname + "=";
            var ca = document.cookie.split(';');
            for(var i=0; i<ca.length; i++) {
               var c = ca[i];
               while (c.charAt(0)==' ') c = c.substring(1);
               if(c.indexOf(name) == 0)
                  return c.substring(name.length,c.length);
            }
            return "";
       }
       
        $.ajax({
            url:$this.attr("href"),
            type:"DELETE",
            dataType:"json",
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
            },
            success:(res)=>{
                if(res.message==='success'){
                    $this.parents('.record').fadeOut("slow",()=>{
                        $this.parents('.record').remove();
                    })
                };
            },
            error:(res)=>{
                alert(res.message);
            }
        })
    }
    return false;
})