addEventListener("load",function(){
    buttonleft=document.getElementsByClassName('navigate-left')[0];
    buttonright = document.getElementsByClassName('navigate-right')[0];
    
    g=function(){
        wholeslide=document.getElementsByClassName("present")[0];
        totalheight=wholeslide.offsetHeight;
        re0=42;
        d=document.getElementsByClassName("slide present")[0];
        for(var i=0;i<d.childNodes.length;i++){
            if(d.childNodes[i].className=="content"){
                var content=d.childNodes[i];
            };
            for(var j=1;j<10;j++){
                if(d.childNodes[i].className=="title"+j){
                    var title=d.childNodes[i];
                    break;
                }
            }
        };
        var left=0;
        var right=re0;
        var fontSize;
        while(left!=right){
            fontSize=Math.ceil((right+left)/2);
            content.style.fontSize = fontSize+"px";
            if(content['offsetHeight']<content['scrollHeight']){
                right=fontSize-1;
            } else{
                left=fontSize;
            }
        }
    };
    g();
    buttonleft.onclick = g;
    buttonright.onclick = g;
});

"addEventListener(\"load\",function(){buttonleft=document.getElementsByClassName('navigate-left')[0];buttonright = document.getElementsByClassName('navigate-right')[0];g=function(){wholeslide=document.getElementsByClassName(\"present\")[0];totalheight=wholeslide.offsetHeight;re0=42;d=document.getElementsByClassName(\"slide present\")[0];for(var i=0;i<d.childNodes.length;i++){if(d.childNodes[i].className==\"content\"){var content=d.childNodes[i];};for(var j=1;j<10;j++){if(d.childNodes[i].className==\"title\"+j){var title=d.childNodes[i];break;}}};var left=0;var right=re0;var fontSize;while(left!=right){fontSize=Math.ceil((right+left)/2);content.style.fontSize = fontSize+'px';if(content['offsetHeight']<content['scrollHeight']){right=fontSize-1;} else{left=fontSize;}}};g();buttonleft.onclick = g;buttonright.onclick = g;});"