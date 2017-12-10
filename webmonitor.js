// function to generate an unique identifier
function generateUUID() {
    "Function for generating unique identifiers"
    var d = new Date().getTime();
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (d + Math.random()*16)%16 | 0;
        d = Math.floor(d/16);
        return (c=='x' ? r : (r&0x3|0x8)).toString(16);
    });
    return uuid;
};

// function to set contact identifier
function setContactID(){
    if(sessionStorage.getItem('uuid') == null){
        sessionStorage.setItem('uuid', generateUUID());
    }
}

// function to add a web page access (url and date)
function setPageAccess(url, date){
    sessionStorage.setItem('url', url);
    sessionStorage.setItem('date', date);
}

// function send request to our application
function sendRequest(){
    console.log("send request");
}