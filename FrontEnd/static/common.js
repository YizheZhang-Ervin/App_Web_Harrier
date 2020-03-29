function changeiframe(){
    ipt001 = document.getElementById('ipt001');
    ifm001 = document.getElementById('ifm001');
    url = ipt001.value;
    if (url.substr(0,4) != "http"){
        url = "http://" + url
    }
    ifm001.src = url;
}